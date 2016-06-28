#encoding "utf-8"

CustomerSellsWord -> Word<kwtype="продать_слово", gram="inpraes">;

CustomerSellsAction -> CustomerSellsWord interp(CustomerSells.Word);
CustomerSellsAction -> CustomerSellsWord interp(CustomerSells.Word) AnyWord<wff=/\d{1,2}/> interp(CustomerSells.Matter);
