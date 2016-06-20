#encoding "utf-8"

PawnWord -> Word<kwtype="ломбард_слово">;

PawnAction -> PawnWord interp(Pawn.Word);
PawnAction -> PawnWord interp(Pawn.Word) Word<kwtype="matter"> interp(Pawn.Matter);
