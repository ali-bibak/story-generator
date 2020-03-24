%{
#include <iostream>
#include "parser.tab.h"
using namespace std;
#define YY_DECL extern "C" int yylex()

%}
%%


q|w|e|r|t|y|i|o|p|a|s|d|f|g|h|j|k|l|z|x|c|v|b|n|m|" "|"\n"|"\t" ;

vaaghe|kheyli|ehtemaalan {
	yylval.adv = strdup(yytext);
	return ADV;
}
gerefte {
	yylval.v_pp = strdup(yytext);
	return V_PP;
}
in {
	yylval.det = strdup(yytext);
	return DET;
}
daarm|mizand|ast|mishavad|mikonad|enad|mikonam|nadaariad {
	yylval.v_prs = strdup(yytext);
	return V_PRS;
}
zanhaye|ruzha|haaye {
	yylval.n_pl = strdup(yytext);
	return N_PL;
}
hum {
	yylval.intt = strdup(yytext);
	return INTT;
}
. {
	yylval.delm = strdup(yytext);
	return DELM;
}
khud|jenaabaali|miman|shomaa|maraa {
	yylval.pro = strdup(yytext);
	return PRO;
}
begirad|nakonm|konam|konid {
	yylval.v_sub = strdup(yytext);
	return V_SUB;
}
cheraa {
	yylval.adv_i = strdup(yytext);
	return ADV_I;
}
shod|jost|roft|kord {
	yylval.v_pa = strdup(yytext);
	return V_PA;
}
bejaai|dar|baa|zemn|beh|bor|az {
	yylval.p = strdup(yytext);
	return P;
}
neh {
	yylval.adv_neg = strdup(yytext);
	return ADV_NEG;
}
raa {
	yylval.clitic = strdup(yytext);
	return CLITIC;
}
pas {
	yylval.adv_time = strdup(yytext);
	return ADV_TIME;
}
davat|ruye|chaman|sahne|ehsaas|movzu|kodaam|ye|lobb|sabab|labkhand|jaanm|estenbaat|donyaai|vahshat|tamaashaai|sarmaa|pul|sharmsaari|hajv|mimi|heyf|tafaavot|ghiyaafe|tasavvor|baar|ghasd|khodaai|gir|javaab|faryaad|ton|sheddat|dast|sedaai|khoshunat|paa|ghollaab|semat|kif|entezaar|lebaas|taajer|shenaa|baavar {
	yylval.n_sing = strdup(yytext);
	return N_SING;
}
mokhtasari|kuchak|naahanjaar|dorosti|kom|namaayeshi|farangi|herafhaye|juan {
	yylval.adj = strdup(yytext);
	return ADJ;
}
ham|voli|koh|inke|va|ammaa {
	yylval.con = strdup(yytext);
	return CON;
}
%%