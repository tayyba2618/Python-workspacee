import datetime

# Email class stores all information related to an email
class Email:
    def __init__(self, sender, receiver, subject, body):
        # Store the sender, receiver, subject, and body of the email
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.body = body

        # Store the current date and time when the email is created
        self.timestamp = datetime.datetime.now()

        # By default, every new email is unread
        self.read = False

    # Mark the email as read
    def mark_as_read(self):
        self.read = True

    # Display the complete email details
    def display_full_email(self):
        # Mark the email as read when it is opened
        self.mark_as_read()

        print('\n--- Email ---')
        print(f'From: {self.sender.name}')
        print(f'To: {self.receiver.name}')
        print(f'Subject: {self.subject}')
        print(f"Received: {self.timestamp.strftime('%Y-%m-%d %H:%M')}")
        print(f'Body: {self.body}')
        print('------------\n')

    # Return a short summary of the email
    def __str__(self):
        # Display "Read" or "Unread" based on the email status
        status = 'Read' if self.read else 'Unread'

        return (
            f"[{status}] From: {self.sender.name} | "
            f"Subject: {self.subject} | "
            f"Time: {self.timestamp.strftime('%Y-%m-%d %H:%M')}"
        )


# User class represents a user with a personal inbox
class User:
    def __init__(self, name):
        # Store the user's name
        self.name = name

        # Create an empty inbox for the user
        self.inbox = Inbox()

    # Send an email to another user
    def send_email(self, receiver, subject, body):

        # Create a new Email object
        email = Email(
            sender=self,
            receiver=receiver,
            subject=subject,
            body=body
        )

        # Add the email to the receiver's inbox
        receiver.inbox.receive_email(email)

        print(f'Email sent from {self.name} to {receiver.name}!\n')

    # Display the user's inbox
    def check_inbox(self):
        print(f"\n{self.name}'s Inbox:")
        self.inbox.list_emails()

    # Read an email by its number
    def read_email(self, index):
        self.inbox.read_email(index)

    # Delete an email by its number
    def delete_email(self, index):
        self.inbox.delete_email(index)


# Inbox class manages all emails for a user
class Inbox:
    def __init__(self):
        # Create an empty list to store emails
        self.emails = []

    # Add a new email to the inbox
    def receive_email(self, email):
        self.emails.append(email)

    # Display all emails in the inbox
    def list_emails(self):

        # Check if the inbox is empty
        if not self.emails:
            print('Your inbox is empty.\n')
            return

        print('\nYour Emails:')

        # Display each email with a number starting from 1
        for i, email in enumerate(self.emails, start=1):
            print(f'{i}. {email}')

    # Read an email
    def read_email(self, index):

        # Check if the inbox is empty
        if not self.emails:
            print('Inbox is empty.\n')
            return

        # Convert the user's email number to a list index
        actual_index = index - 1

        # Check whether the email number is valid
        if actual_index < 0 or actual_index >= len(self.emails):
            print('Invalid email number.\n')
            return

        # Display the selected email
        self.emails[actual_index].display_full_email()

    # Delete an email
    def delete_email(self, index):

        # Check if the inbox is empty
        if not self.emails:
            print('Inbox is empty.\n')
            return

        # Convert the user's email number to a list index
        actual_index = index - 1

        # Check whether the email number is valid
        if actual_index < 0 or actual_index >= len(self.emails):
            print('Invalid email number.\n')
            return

        # Remove the selected email from the inbox
        del self.emails[actual_index]

        print('Email deleted.\n')


# Main function to demonstrate the email simulator
def main():

    # Create two users
    tory = User('Tory')
    ramy = User('Ramy')

    # Tory sends an email to Ramy
    tory.send_email(
        ramy,
        'Hello',
        'Hi Ramy, just saying hello!'
    )

    # Ramy replies to Tory
    ramy.send_email(
        tory,
        'Re: Hello',
        'Hi Tory, hope you are fine.'
    )

    # Ramy checks his inbox
    ramy.check_inbox()

    # Ramy reads the first email
    ramy.read_email(1)

    # Ramy deletes the first email
    ramy.delete_email(1)

    # Ramy checks his inbox again after deleting the email
    ramy.check_inbox()


# Run the program only if this file is executed directly
if __name__ == '__main__':
    main()