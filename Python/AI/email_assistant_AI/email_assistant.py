
# Third part
from dotenv import load_env
import aisuite as ai
import json

# local file
import utils
import display_functions
import email_tools

# ================================
# Environment & Client
# ================================

load_dotenv() # Load environment variables from .env
client = ai.Client()

"""This lab uses a simulated email backend to mimic real-world email interactions. Think of it as your personal sandbox email inbox: it comes preloaded with messages so you can practice without sending real emails."""

"""
Layer	            Purpose
--------------------------------
FastAPI	            Exposes REST endpoints (server)
SQLite + SQLAlchemy	Stores and queries emails locally (database)
Pydantic	        Ensures inputs and outputs are valid (schema)
AISuite tools	    Bridge between the LLM and the service (tools)
"""


"Endpoints: The service provides several routes that simulate common email actions."
"""
    POST /send → send a new email
    GET /emails → list all emails
    GET /emails/unread → show only unread emails
    GET /emails/{id} → fetch a specific email by ID
    GET /emails/search?q=... → search emails by keyword
    GET /emails/filter → filter by recipient or date range
    PATCH /emails/{id}/read → mark an email as read
    PATCH /emails/{id}/unread → mark an email as unread
    DELETE /emails/{id} → delete an email by ID
    GET /reset_database → reset emails to initial state (for testing)
"""

"Before giving control to the LLM, you’ll first test the backend yourself. The utils.test_* functions are quick wrappers around the API endpoints. They let you try actions like send, list, search, filter, mark, and delete without writing raw HTTP requests."
"given in the utils.py file."

"""
    For example, you can test:
    -Send a test email
    -Fetch email by ID
    -List all messages
    -Mark email as read or unread
    -Delete email
"""

# uncomment the line 'utils.test_*' you want to try
new_email_id = utils.test_send_email()
_ = utils.test_get_email(new_email_id['id'])
#_ = utils.test_list_emails()
#_ = utils.test_filter_emails(recipient="test@example.com")
#_ = utils.test_search_emails("lunch")
#_ = utils.test_unread_emails()
#_ = utils.test_mark_read(new_email_id['id'])
#_ = utils.test_mark_unread(new_email_id['id'])
#_ = utils.test_delete_email(new_email_id['id'])
#_ = utils.reset_database()

"""
    Tool Function	                Action
    list_all_emails()	            Fetch all emails, newest first
    list_unread_emails()	        Retrieve only unread emails
    search_emails(query)	        Search by keyword in subject, body, or sender
    filter_emails(...)	            Filter by recipient and/or date range
    get_email(email_id)	            Fetch a specific email by ID
    mark_email_as_read(id)	        Mark an email as read
    mark_email_as_unread(id)	    Mark an email as unread
    send_email(...)	                Send a new (simulated) email
    delete_email(id)	            Delete an email by ID
    search_unread_from_sender(addr)	Return unread emails from a given sender (e.g., boss@email.com)
"""

# Test sending a new email and fetch it by ID
new_email = email_tools.send_email("test@example.com", "Lunch plans", "Shall we meet at noon?")
content_ = email_tools.get_email(new_email['id'])

# Uncomment the ones you want to try:
#content_ = email_tools.list_all_emails()
#content_ = email_tools.list_unread_emails()
#content_ = email_tools.search_emails("lunch")
#content_ = email_tools.filter_emails(recipient="test@example.com")
#content_ = email_tools.mark_email_as_read(new_email['id'])
#content_ = email_tools.mark_email_as_unread(new_email['id'])
#content_ = email_tools.search_unread_from_sender("test@example.com")
#content_ = email_tools.delete_email(new_email['id'])

utils.print_html(content=json.dumps(content_, indent=2), title="Testing the email_tools")



def build_prompt(request_: str) -> str:
    return f"""
    - You are an AI assistant specialized in managing emails.
    - You can perform various actions such as listing, searching, filtering, and manipulating emails.
    - Use the provided tools to interact with the email system.
    - Never ask the user for confirmation before performing an action.
    - If needed, my email address is "you@email.com" so you can use it to send emails or perform actions related to my account.

    {request_.strip()}
    """


example_prompt = build_prompt("Delete the Happy Hour email")
utils.print_html(content=example_prompt, title="Example example_prompt")

utils.reset_database()


# Try your own requests
prompt_ = build_prompt("Check for unread emails from boss@email.com, mark them as read, and send a polite follow-up.")

response = client.chat.completions.create(
    model="openai:gpt-4.1", # LLM
    messages=[{"role": "user", "content": (
        prompt_
    )}],
    tools=[ # list of tools that the LLM can access
        email_tools.search_unread_from_sender,
        email_tools.list_unread_emails,
        email_tools.search_emails,
        email_tools.get_email,
        email_tools.mark_email_as_read,
        email_tools.send_email
    ],
    max_turns=5,
)

display_functions.pretty_print_chat_completion(response)

