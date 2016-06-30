#encoding "utf8"

TabletWord -> Word<kwtype="планшет_слово">;

TabletVendorRus -> Word<kwtype="планшет_производитель_рус">;
TabletVendorEng -> Word<kwtype="планшет_производитель_англ">;
TabletVendor -> TabletVendorRus | TabletVendorEng;

TabletModel -> UnknownPOS* AnyWord<wff=/(\d+)|(\w\d)|(\d\w)/>;

TabletUserDefinedName -> AnyWord<kwtype='**планшет_пользовательское_название**'>;

S -> TabletWord (TabletVendor) (TabletModel) (TabletWord);
S -> (TabletWord) TabletVendor (TabletModel) (TabletWord);
S -> TabletVendor TabletWord; // асус планшет
S -> TabletUserDefinedName (TabletVendor) (TabletWord);
S -> TabletUserDefinedName;
S -> (TabletWord) TabletUserDefinedName;
