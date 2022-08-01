from src import db
from src.models.Account import Account
from src.models.Notification import Notification
from src.models.NotificationAccount import NotificationAccount

def saveNotification(dataNotificationRequest):
    response = None
    # confirm if account exists
    account = Account.query.filter_by(id=dataNotificationRequest['account_id']).first()
    print(account)
    if account == None:
        return {
           'status': '400',
            'message': 'Tentativa de notificação para conta inexistente'
        }

    try:
        # init notification
        notification = Notification(dataNotificationRequest['message'])
        # save notification
        db.session.add(notification)
        db.session.flush()

        # init notificationAccount
        notificationAccount = NotificationAccount(notification.id, account.id)

        # save notificationAccount
        db.session.add(notificationAccount)
        db.session.commit()

        response = {
            'status': '200',
            'message': 'Notificação salva com sucesso'
        }
    except Exception as e:
        db.session.rollback()
        print(e)
        response =  {
            'status': '400',
            'message': 'Um erro inesperável ocorreu. Caso persista, entre em contato com o administrador do sistema', 
            'error': str(e)
        }

    return response

def getNotificationById(notificationId):
    response = None

    notification = Notification.query.filter_by(id=notificationId).first()

    if notification:
        data = {
            "id": notification.id,
            "message": notification.message
        }
        response = {
            'status': '200',
            'message': 'Registro recuperado com sucesso',
            'data': data
        }
    else:
        response = {
            'status': '400',
            'message': 'Nenhum registro encontrado'
        }

    return response