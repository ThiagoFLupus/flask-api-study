from src import db
from src.models.Account import Account
from src.models.User import User

def saveAccount(dataAccountRequest):
    response = None
    try:
        # init model Account object
        account = Account(
            dataAccountRequest['business_name'], 
            dataAccountRequest['status']
        )

        # add account to transaction
        db.session.add(account)
        db.session.flush()

        # init model User object
        user = User(
            dataAccountRequest['email'], 
            dataAccountRequest['name'], 
            dataAccountRequest['password'], 
            dataAccountRequest['permission_level'], 
            account.id
        )

        # add user to transaction
        db.session.add(user)

        # commit all
        db.session.commit()

        # format response
        response = {
            'status': '200',
            'message': 'success',
        }
    except Exception as e:
        db.session.rollback()
        response =  {
            'status': '400',
            'message': 'Um erro inesperável ocorreu. Caso persista, entre em contato com o administrador do sistema', 
            'error': str(e)
        }

    return response

def getAccounts():
    response = None

    accounts = Account.query.all()
    dataAccount = []
    if len(accounts) > 0:
        for account in accounts:
            accountObj = {
                "business_name": account.business_name,
                "status": account.status,
            }
            dataAccount.append(accountObj)
        
        response = {
            'status': '200',
            'message': 'success',
            'data': dataAccount
        }
        return response
    else:
        response = {
            'status': '200',
            'message': 'success',
            'data': []
        }
def getAccountById(accountId):
    response = None

    account = Account.query.filter_by(id=accountId).first()

    if account:
        users = User.query.filter_by(account_id=account.id).all()
        dataUser = []
        if len(users) > 0:
            for user in users:
                userObj = {
                    "email": user.email,
                    "name": user.name,
                    "password": user.password, 
                    "permission_level": user.permission_level,
                    "created_at": user.created_at
                }
                dataUser.append(userObj)

        data = {
            "id": account.id,
            "business_name": account.business_name,
            "status": account.status,
            "users": dataUser,
            "created_at": account.created_at,
            "updated_at": account.updated_at
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

def updateAccount(dataAccount):
    response = None

    # get register by id
    account = Account.query.filter_by(id=dataAccount['id']).first()
    if account == None:
        response = {
            'status': '400',
            'message': 'Nenhum dado encontrado, para ser atualizado'
        }
    else:
        # update
        try:
            account.business_name = dataAccount['business_name']
            account.status = dataAccount['status']

            db.session.commit()

            data = {
                "id": account.id,
                "business_name": account.business_name,
                "status": account.status
            }

            response = {
                'status': 200,
                'message': 'Conta atualizada com sucesso',
                'data': data
            }
        except Exception as e:
            db.session.rollback()
            print(e)
            response = {
                'status': '400',
                'message': 'Um erro inesperado ocorreu. Se persistir, contate o administrador do sistema'
            }

    return response