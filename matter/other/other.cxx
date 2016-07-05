#encoding "utf8"

//SpecificMatter -> Adj<gnc-agr[1]> Noun<gnc-agr[1]>;

Console -> AnyWord<wff=/(([Pp]s|[Пп]с)\d)|((xbox|хбо[хкс])(360|720)?)/>;

Photocamera -> Word<kwtype="фотоаппарат_слово">;
OtherWord -> AnyWord<kwtype="другой_предмет_слово">;
OtherWord -> Console;

OtherVendorRus -> Word<kwtype="другой_предмет_производитель_рус">;
OtherVendorEng -> Word<kwtype="другой_предмет_производитель_англ">;
OtherVendor -> OtherVendorRus | OtherVendorEng;

OtherUserDefinedName -> AnyWord<kwtype="другой_предмет_пользовательское_название">;

//S -> SpecificMatter;
S -> Photocamera;
S -> OtherWord (OtherVendor) (OtherWord);
S -> (OtherWord) OtherVendor (OtherWord);
S -> OtherUserDefinedName (OtherVendor) (OtherWord);
S -> (OtherVendor) OtherUserDefinedName;
S -> OtherUserDefinedName;
