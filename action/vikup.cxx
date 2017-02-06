#encoding "utf-8"

CustomerSellsWord -> Verb<kwtype="продать_слово", gram="непрош"> ;
CustomerSellsWord -> Word<kwtype="продать_слово">;

CustomerSellsAction -> CustomerSellsWord interp(ActionType.Sell);
