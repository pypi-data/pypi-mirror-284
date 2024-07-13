import automationassets  # type: ignore
from sync_mailchimp_entra.core.mailchimp import MailchimpClient
from sync_mailchimp_entra.core.graph import GraphClient
from kiota_abstractions.api_error import APIError
import json
import ast
from sync_mailchimp_entra.utils.progress_bar import ProgressBar


async def mailchimp_entra(list_mailchimp_id, entra_groups_ids):
    """Main synchronization function."""

    members_mailchimp_emails = MailchimpClient.get_instance().list_mailchimp_emails(
        list_mailchimp_id
    )

    members_entra_emails = {}
    for entra_group_id in entra_groups_ids:
        entra_emails = await GraphClient.get_instance(
            automationassets.get_automation_variable(f"TENANT{entra_group_id[1]}_ID"),
            automationassets.get_automation_variable(
                f"TENANT{entra_group_id[1]}_APPLICATION_ID"
            ),
            automationassets.get_automation_variable(
                f"TENANT{entra_group_id[1]}_APPLICATION_SECRET"
            ),
            ["https://graph.microsoft.com/.default"],
        ).list_entra_emails(entra_group_id[0])
        for email in ProgressBar(
            entra_emails, prefix="Process Entra mails:", length=50
        ):
            email_domains = json.loads(
                automationassets.get_automation_variable("MAIL_DOMAINS")
            )
            validated = False
            i = 0
            while not validated and i != len(email_domains):
                if email_domains[i] in email.lower():
                    members_entra_emails[email] = f"{entra_group_id[1]}"
                    validated = True
                i += 1
            if not validated:
                if automationassets.get_automation_variable("DEBUG") == "1":
                    print(f"{email} not in email domains.")

    entra_emails = list(members_entra_emails.keys())

    # Iteration on every MailChimp mail to see if it is in Entra
    for email in ProgressBar(
        members_mailchimp_emails, prefix="Process Mailchimp users:", length=50
    ):
        if email.lower() not in [x.lower() for x in entra_emails]:
            MailchimpClient().get_instance().remove_member(list_mailchimp_id, email)
            if automationassets.get_automation_variable("DEBUG") == "1":
                print(email + " removed from MailChimp mails.")

    # Iteration on every Entra mail to see if it is in MailChimp list
    for email in ProgressBar(entra_emails, prefix="Process Entra users:", length=50):
        # Get user data from Graph
        user = None
        try:
            user = await GraphClient.get_instance().get_user(email)
        except APIError:
            try:
                user = await GraphClient.get_instance(
                    automationassets.get_automation_variable(
                        f"TENANT{members_entra_emails[email]}_ID"
                    ),
                    automationassets.get_automation_variable(
                        f"TENANT{members_entra_emails[email]}_APPLICATION_ID"
                    ),
                    automationassets.get_automation_variable(
                        f"TENANT{members_entra_emails[email]}_APPLICATION_SECRET"
                    ),
                    ["https://graph.microsoft.com/.default"],
                ).get_user(email)
            except APIError as e:
                if "Request_ResourceNotFound" == e.error.code:
                    if automationassets.get_automation_variable("DEBUG") == "1":
                        print(
                            f"The user {email} has probably been invited on to the tenant, so that the mail of the user is not an id."
                        )
                else:
                    raise
            # Get correct language for user
            if user:
                if hasattr(user, "company_name") and user.company_name:
                    companies_languages = ast.literal_eval(
                        automationassets.get_automation_variable("COMPANIES_LANGUAGES")
                    )
                    entra_language = companies_languages.get(
                        user.company_name.upper(), "fr"
                    )
                    if email.lower() not in [
                        x.lower() for x in members_mailchimp_emails
                    ]:
                        # Addition of user in MailChimp
                        if (not (hasattr(user, "given_name"))) or (
                            not (hasattr(user, "surname"))
                        ):
                            MailchimpClient().get_instance().add_member(
                                list_mailchimp_id, email, language=entra_language
                            )
                        else:
                            MailchimpClient().get_instance().add_member(
                                list_mailchimp_id,
                                email,
                                first_name=user.given_name,
                                last_name=user.surname,
                                language=entra_language,
                            )
                    else:
                        mailchimp_language = (
                            MailchimpClient()
                            .get_instance()
                            .get_member_language(list_mailchimp_id, email.lower())
                        )
                        if mailchimp_language != entra_language:
                            MailchimpClient().get_instance().update_member(
                                list_mailchimp_id, email, language=entra_language
                            )
                else:
                    if automationassets.get_automation_variable("DEBUG") == "1":
                        print(f"Company not found for user {email}.")
                    entra_language = "fr"
