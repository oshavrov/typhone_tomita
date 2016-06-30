#encoding "utf-8"

CustomerSellsWord -> Word<kwtype="продать_слово">;
CustomerSellsWord -> Verb<kwtype="продать_слово", gram="inpraes">;

CustomerSellsAction -> CustomerSellsWord interp(CustomerSells.Word);
