from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def enviar_notificacao_anexo(leiloeiro, anexo):
    subject = 'Novo Anexo Adicionado'
    html_message = render_to_string('core/email_notificacao.html', {'leiloeiro': leiloeiro, 'anexo': anexo})
    plain_message = strip_tags(html_message)
    from_email = 'webmaster@example.com'
    to = leiloeiro.email

    send_mail(subject, plain_message, from_email, [to], html_message=html_message)
