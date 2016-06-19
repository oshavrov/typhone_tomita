#encoding "utf8"

PhoneWord -> Word<kwtype="телефон_слово">;

PhoneVendorRus -> Word<kwtype="телефон_производитель_рус">;
PhoneVendorEng -> Word<kwtype="телефон_производитель_англ">;
PhoneVendor -> PhoneVendorRus | PhoneVendorEng;

PhoneModel -> UnknownPOS+ AnyWord<wfl=/(\w{0,8}\d{0,8})|(\d{0,8}\w{0,8})/>;

PhoneUserDefinedName -> AnyWord<kwtype="телефон_пользовательское_название">;

S -> PhoneWord interp(Phone.Word) (PhoneVendor interp(Phone.Vendor)) (PhoneModel interp(Phone.Model));
S -> (PhoneWord interp(Phone.Word)) PhoneVendor interp(Phone.Vendor) (PhoneModel interp(Phone.Model));
S -> PhoneUserDefinedName interp(Phone.UserDefinedName);