#encoding "utf8"

//SpecificMatter -> Adj<gnc-agr[1]> Noun<gnc-agr[1]>;
OtherWord -> AnyWord<kwtype="другой_предмет_слово">;
OtherVendorRus -> Word<kwtype="другой_предмет_производитель_рус">;
OtherVendorEng -> Word<kwtype="другой_предмет_производитель_англ">;
OtherVendor -> OtherVendorRus | OtherVendorEng;
OtherUserDefinedName -> AnyWord<kwtype="другой_предмет_пользовательское_название">;

//S -> SpecificMatter;
S -> OtherWord (OtherVendor) (OtherWord);
S -> (OtherWord) OtherVendor (OtherWord);
S -> OtherUserDefinedName (OtherVendor) (OtherWord);
S -> (OtherVendor) OtherUserDefinedName;
S -> OtherUserDefinedName;
