
from django.contrib import admin
from django.contrib import messages
from route.models import Bin, CustomUser, Stock


# Register your models here.

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id','email','username')
    list_display_links = ('id','username')

class BinAdmin(admin.ModelAdmin):
    list_display = ('product_code','product_color','initalQty','qty','litre','list_date','updateQuantity')
    list_display_links = ('product_code','qty')
    list_editable = ('updateQuantity',)


    actions = ["update_selected_Stock","Send_fresh_stock","Send_updated_bin_to_stock"]

    def update_selected_Stock(self,request,queryset):
        
        for bin in queryset:
            u = Stock.objects.filter(product_code = bin.product_code)
            
            if bin.status == "Pending":
                e = int(bin.updateQuantity)
                bin.qty += e
                update = queryset.update(qty=bin.qty)


    def Send_fresh_stock(self,request,queryset):

        for data in queryset:
            all_data = Stock()

            if data.status == "Pending":
                all_data.product_code = data.product_code
                all_data.color_type = data.product_color
                all_data.litre = data.litre
                all_data.qty_receieved = data.initalQty
                all_data.qty_balance = data.initalQty
                all_data.officer = request.user.username
                all_data.client_name = data.client_name
                all_data.save()

                
    
    def Send_updated_bin_to_stock(self,request,queryset):

        for data in queryset:
            all_data = Stock()

            if data.status == "Pending":
                all_data.product_code = data.product_code
                all_data.color_type = data.product_color
                all_data.litre = data.litre
                all_data.qty_receieved = data.updateQuantity
                all_data.qty_balance = data.qty
                all_data.officer = request.user.username
                all_data.save()


            

        
                


class StokeAdmin(admin.ModelAdmin):
    list_display = ('product_code','litre','client_name','created','status')
    list_display_links = ('product_code','litre','status')

    actions = ['approve_stock',] 

    def approve_stock(self,request,queryset):

        for stock in queryset:
            u = Bin.objects.get(product_code = stock.product_code,litre=stock.litre)

            if stock.status == "Pending":
                e = int(stock.qty_issued)
                # update = queryset.update(qty_receieved=u.qty)
                u.qty -= e
                u.save()
                update = queryset.update(status="Approved")
                update = queryset.update(qty_balance=u.qty)


admin.site.register(Stock,StokeAdmin)
admin.site.register(Bin,BinAdmin)
admin.site.register(CustomUser,CustomUserAdmin)