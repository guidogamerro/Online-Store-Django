def import_total_cart(request): 

    total = 0

    #if request.user.is_authenticated: ##luego usaremos esta line

    for key, value in request.session["cart"].items():

        total = total + float(value["price"])
 
    return {"import_total_cart": total}