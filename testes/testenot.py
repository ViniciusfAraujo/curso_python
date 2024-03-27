from winotify import Notification

notificacao = Notification(
    app_id="Codigo em Python", 
    title="Notificação",
    msg="Ola Pycoder",
    icon=r"C:\Users\User\Pictures\fotosport/logo-python.png"
)

notificacao.show()




























# from win10toast import ToastNotifier

# toaster = ToastNotifier()

# toaster.show_toast(
#     "Olá mundo!!!",
#     "Python tem 10 segundos awsm!",
#     threaded=True,
#     icon_path="custon.icon",
#     duração=10
# )

# toaster.show_toast(
#     "Exemplo dois",
#     "Esta notificação está em seu próprio tópico!",
#     icon_path=None,
#     Duration=5,
#     threaded=True
# )

