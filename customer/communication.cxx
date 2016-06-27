#encoding "utf-8"

Call -> Word<kwtype="call"> interp(Communication.Call);
SMS -> Word<kwtype="sms"> interp(Communication.SMS);
WA -> Word<kwtype="whatsapp"> interp(Communication.WhatsApp);

S -> Call;
S -> SMS;
S -> WA;