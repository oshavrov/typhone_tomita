#encoding "utf8"

PhoneWord -> Word<kwtype="телефон_слово">;

PhoneVendorRus -> Word<kwtype="телефон_производитель_рус">;
PhoneVendorEng -> Word<kwtype="телефон_производитель_англ">;
PhoneVendor -> PhoneVendorRus | PhoneVendorEng;

S -> PhoneWord interp(Phone.Word) (PhoneVendor interp(Phone.Vendor));
S -> (PhoneWord interp(Phone.Word)) PhoneVendor interp(Phone.Vendor);