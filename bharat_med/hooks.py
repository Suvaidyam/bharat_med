
app_name = "bharat_med"
app_title = "Bharat Med"
app_publisher = "Ajamat"
app_description = "life enjoying"
app_email = "ajamatansari86@gmail.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "bharat_med",
# 		"logo": "/assets/bharat_med/logo.png",
# 		"title": "Bharat Med",
# 		"route": "/bharat_med",
# 		"has_permission": "bharat_med.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/bharat_med/css/bharat_med.css"
# app_include_js = "/assets/bharat_med/js/bharat_med.js"

# include js, css files in header of web template
# web_include_css = "/assets/bharat_med/css/bharat_med.css"
# web_include_js = "/assets/bharat_med/js/bharat_med.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "bharat_med/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "bharat_med/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# automatically load and sync documents of this doctype from downstream apps
# importable_doctypes = [doctype_1]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "bharat_med.utils.jinja_methods",
# 	"filters": "bharat_med.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "bharat_med.install.before_install"
# after_install = "bharat_med.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "bharat_med.uninstall.before_uninstall"
# after_uninstall = "bharat_med.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "bharat_med.utils.before_app_install"
# after_app_install = "bharat_med.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "bharat_med.utils.before_app_uninstall"
# after_app_uninstall = "bharat_med.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "bharat_med.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"bharat_med.tasks.all"
# 	],
# 	"daily": [
# 		"bharat_med.tasks.daily"
# 	],
# 	"hourly": [
# 		"bharat_med.tasks.hourly"
# 	],
# 	"weekly": [
# 		"bharat_med.tasks.weekly"
# 	],
# 	"monthly": [
# 		"bharat_med.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "bharat_med.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "bharat_med.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "bharat_med.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["bharat_med.utils.before_request"]
# after_request = ["bharat_med.utils.after_request"]

# Job Events
# ----------
# before_job = ["bharat_med.utils.before_job"]
# after_job = ["bharat_med.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"bharat_med.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }


website_route_rules = [{'from_route': '/frontend/<path:app_path>', 'to_route': 'frontend'},]