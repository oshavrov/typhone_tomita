#encoding "utf-8"

CustomerBuysWord -> Word<kwtype="купить_слово">;

CustomerBuysAction -> CustomerBuysWord interp(ActionType.Buy);
CustomerBuysAction -> CustomerBuysWord interp(ActionType.Buy) AnyWord<wff=/\d{1,2}/> interp(ActionType.Buy);