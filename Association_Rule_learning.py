
#########################
# Association Rule Based Recommender System
#########################

#########################
# İş Problemi
#########################
# Aşağıda 3 farklı kullanıcının sepet bilgileri verilmiştir. Bu sepet bilgilerine en
# uygun ürün önerisini birliktelik kuralı kullanarak yapınız. Ürün önerileri 1 tane
# ya da 1'den fazla olabilir. Karar kurallarını 2010-2011 Germany müşterileri
# üzerinden türetiniz

# Kullanıcı 1’in sepetinde bulunan ürünün id'si: 21987
# Kullanıcı 2’in sepetinde bulunan ürünün id'si : 23235
# Kullanıcı 3’in sepetinde bulunan ürünün id'si : 22747

#########################
# Veri Seti
#########################
# Online Retail II isimli veri seti İngiltere merkezli bir perakende şirketinin 01/12/2009 - 09/12/2011 tarihleri arasındaki online satış
# işlemlerini içeriyor. Şirketin ürün kataloğunda hediyelik eşyalar yer almaktadır ve çoğu müşterisinin toptancı olduğu bilgisi
# mevcuttur.

# 8 Değişken 541.909 Gözlem 45.6MB
# InvoiceNo Fatura Numarası ( Eğer bu kod C ile başlıyorsa işlemin iptal edildiğini ifade eder )
# StockCode Ürün kodu ( Her bir ürün için eşsiz )
# Description Ürün ismi
# Quantity Ürün adedi ( Faturalardaki ürünlerden kaçar tane satıldığı)
# InvoiceDate Fatura tarihi
# UnitPrice Fatura fiyatı ( Sterlin )
# CustomerID Eşsiz müşteri numarası
# Country Ülke ismi


#########################
# GÖREV 1: Veriyi Hazırlama
#########################
# Adım 1: Online Retail II veri setinden 2010-2011 sheet’ini okutunuz.
# Adım 2: StockCode’u POST olan gözlem birimlerini drop ediniz. (POST her faturaya eklenen bedel, ürünü ifade etmemektedir.)
# Adım 3: Boş değer içeren gözlem birimlerini drop ediniz.
# Adım 4: Invoice içerisinde C bulunan değerleri veri setinden çıkarınız. (C faturanın iptalini ifade etmektedir.)
# Adım 5: Price değeri sıfırdan küçük olan gözlem birimlerini filtreleyiniz.
# Adım 6: Price ve Quantity değişkenlerinin aykırı değerlerini inceleyiniz, gerekirse baskılayınız.



#########################
# GÖREV 2: Alman Müşteriler Üzerinden Birliktelik Kuralları Üretme
#########################
# Adım 2: Aşağıdaki gibi fatura ürün pivot table’i oluşturacak create_invoice_product_df fonksiyonunu tanımlayınız

# Adım 2: Kuralları oluşturacak create_rules fonksiyonunu tanımlayınız ve alman müşteriler için kurallarını bulunuz.
