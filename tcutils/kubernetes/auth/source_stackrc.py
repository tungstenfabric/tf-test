import os


def source_stackrc(user_name='admin', password='password', project_name='admin', domain_name='admin_domain', auth_url=None):
    os.environ['OS_IDENTITY_API_VERSION'] = '3'
    os.environ['OS_USER_DOMAIN_NAME'] = domain_name
    os.environ['OS_USERNAME'] = user_name
    os.environ['OS_PROJECT_DOMAIN_NAME'] = domain_name
    os.environ['OS_PROJECT_NAME'] = project_name
    os.environ['OS_PASSWORD'] = password
    os.environ['OS_AUTH_URL'] = auth_url
    os.environ['OS_DOMAIN_NAME'] = domain_name
