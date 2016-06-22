#encoding "utf-8"

CustomerBuysWord -> Word<kwtype="купить_слово">;

CustomerBuysAction -> CustomerBuysWord interp(CustomerBuys.Word);
CustomerBuysAction -> CustomerBuysWord interp(CustomerBuys.Word) AnyWord<wff=/\d{1,2}/> interp(CustomerBuys.NumberInPrice);