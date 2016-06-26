#encoding "utf-8"
#GRAMMAR_ROOT S


CallPlaceBur -> AnyWord<kwtype="место_бурятия">;
CallPlaceYkt -> AnyWord<kwtype="место_якутия">;

S -> CallPlaceBur interp(CustomerPlace.Buryatia);
S -> CallPlaceYkt interp(CustomerPlace.Yakutia);
