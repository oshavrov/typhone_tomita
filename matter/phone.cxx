#encoding "utf8"

PhoneWord -> Word<kwtype="телефон_слово">;

PhoneVendorRus -> Word<kwtype="телефон_производитель_рус">;
PhoneVendorEng -> Word<kwtype="телефон_производитель_англ">;
PhoneVendor -> PhoneVendorRus | PhoneVendorEng;

PhoneModel -> UnknownPOS* UnknownPOS;
//PhoneModel -> AnyWord<wff=/(([A-Za-z/ -]{0,19}\d)[A-Za-z0-9/ -]{4,20})/>

S -> PhoneWord interp(Phone.Word) (PhoneVendor interp(Phone.Vendor)) (PhoneModel interp(Phone.Model));
S -> (PhoneWord interp(Phone.Word)) PhoneVendor interp(Phone.Vendor) (PhoneModel interp(Phone.Model));