#encoding "utf-8"

CallPlaceBur -> Word<kwtype="место_бурятия">;
CallPlaceYkt -> Word<kwtype="место_якутия">;

S -> CallPlaceBur interp(CustomerPlace.Buryatia);
S -> CallPlaceYkt interp(CustomerPlace.Yakutia);