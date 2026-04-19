import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} fonksiyonu {end - start} saniyede çalıştı.")
        return result
    return wrapper

@timer_decorator
def event(x, y):
    time.sleep(1)
    return x + y

print(event(10, 20))

#########################################################################

current_user = {"role": "user"}

def auth_decorator(needed_role):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if current_user["role"] != needed_role:
                return "Erişim Reddedildi: Yetersiz Yetki"
            return func(*args, **kwargs)
        return wrapper
    return decorator

@auth_decorator("admin")
def gizli_islem():
    return "Gizli veriye erişildi"

print(gizli_islem())

#########################################################################
current_user2 = {"membership": "basic"}

def login_required(membership_type):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if current_user2["membership"] != membership_type:
                return "Erişim Reddedildi: basic üyelik gerekli"
            return func(*args, **kwargs)
        return wrapper
    return decorator

@login_required("basic")
def false_process():
    return "İçeriğe erişildi"

print(false_process())