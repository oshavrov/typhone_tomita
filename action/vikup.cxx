#encoding "utf-8"

CustomerSellsWord -> Word<kwtype="продать_слово">;

CustomerSellsAction -> CustomerSellsWord interp(CustomerSells.Word);
CustomerSellsAction -> CustomerSellsWord interp(CustomerSells.Word) AnyWord<wff=/\d{1,2}/> interp(CustomerSells.Matter);