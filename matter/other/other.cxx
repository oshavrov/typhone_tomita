#encoding "utf8"

//SpecificMatter -> Adj<gnc-agr[1]> Noun<gnc-agr[1]>;

Playstation -> AnyWord<wff=/([Pp]s|[Пп]с)\d?/> (AnyWord<wff=/\d/>);
Xbox -> AnyWord<wff=/([Xxbo]x)|([Хх]бо[хк]с?)((360)|(720))?/> (AnyWord<wff=/(360)|(720)/>);
Console -> Playstation | Xbox;

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
