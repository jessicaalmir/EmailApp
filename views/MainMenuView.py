from tkinter import *
from controllers.EmailTemplateController import EmailTemplateController
from controllers.EmailListController import EmailListController
from controllers.SendEmailController import SendEmailController
from views.MainSendEmailView import MainSendEmailView
from controllers.ReportListController import ReportListController
from controllers.ReportTemplateController import ReportTemplateController
from controllers.reportEmailSentController import ReportEmailSentController

class MainMenu(Frame):

    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        # Menu Definition
        self.menuBar = Menu(self.parent)
        # add menu to window
        self.parent.config(menu=self.menuBar)

        #Emails submenu
        emails_menu = Menu(self.menuBar)
        emails_menu.add_command(label="Templates", command=self.view_email_templates)
        emails_menu.add_command(label="Lists", command=self.view_email_Lists)
        emails_menu.add_command(label="Send Emails", command=self.view_send_email)
        #add Emails menu to the Main Menu
        self.menuBar.add_cascade(label="Emails", menu=emails_menu)

        #Reports submenu
        reports_menu = Menu(self.menuBar)
        reports_menu.add_command(label="Report Templates", command=self.view_reports_template)
        reports_menu.add_command(label="Report List", command=self.view_reports_list)
        reports_menu.add_command(label="Report Sent", command=self.view_emails_sent)
        # add Reports menu to the Main Menu
        self. menuBar.add_cascade(label="Reports", menu=reports_menu)

    #Call Report List
    def view_reports_list(self):
        # block menu bar
        self.menuBar.entryconfig('Reports', state=DISABLED)
        self.menuBar.entryconfigure('Emails', state=DISABLED)
        # Call new Window
        win = ReportListController(self.parent)
        # Enabled menu bar
        self.menuBar.entryconfig('Reports', state=NORMAL)
        self.menuBar.entryconfigure('Emails', state=NORMAL)

    # Call Report Templates
    def view_reports_template(self):
        # block menu bar
        self.menuBar.entryconfig('Reports', state=DISABLED)
        self.menuBar.entryconfigure('Emails', state=DISABLED)
        # Call new Window
        win = ReportTemplateController(self.parent)
        # Enabled menu bar
        self.menuBar.entryconfig('Reports', state=NORMAL)
        self.menuBar.entryconfigure('Emails', state=NORMAL)

    # Call Report Emails Sent
    def view_reports_template(self):
        # block menu bar
        self.menuBar.entryconfig('Reports', state=DISABLED)
        self.menuBar.entryconfigure('Emails', state=DISABLED)
        # Call new Window
        win = ReportTemplateController(self.parent)
        # Enabled menu bar
        self.menuBar.entryconfig('Reports', state=NORMAL)
        self.menuBar.entryconfigure('Emails', state=NORMAL)

    def view_email_templates(self):
        # block menu bar
        self.menuBar.entryconfig('Reports', state=DISABLED)
        self.menuBar.entryconfigure('Emails', state=DISABLED)
        #Call new Window
        win = EmailTemplateController(self.parent)
        #Enabled menu bar
        self.menuBar.entryconfig('Reports', state=NORMAL)
        self.menuBar.entryconfigure('Emails', state=NORMAL)

    def view_emails_sent(self):
        # block menu bar
        self.menuBar.entryconfig('Reports', state=DISABLED)
        self.menuBar.entryconfigure('Emails', state=DISABLED)
        #Call new Window
        win = ReportEmailSentController(self.parent)
        #Enabled menu bar
        self.menuBar.entryconfig('Reports', state=NORMAL)
        self.menuBar.entryconfigure('Emails', state=NORMAL)

    def view_email_Lists(self):
        # block menu bar
        self.menuBar.entryconfig('Reports', state=DISABLED)
        self.menuBar.entryconfigure('Emails', state=DISABLED)
        #Call new Window
        win = EmailListController(self.parent)
        #Enabled menu bar
        self.menuBar.entryconfig('Reports', state=NORMAL)
        self.menuBar.entryconfigure('Emails', state=NORMAL)

    def view_send_email(self):
        # Call new Window
        emailController = SendEmailController(self.parent)
        emailController.GetDataList()
        view = MainSendEmailView(self.parent, emailController.listEmailList, emailController.listEmailTemplate)

        # Enabled menu bar
        self.menuBar.entryconfig('Reports', state=NORMAL)
        self.menuBar.entryconfigure('Emails', state=NORMAL)


