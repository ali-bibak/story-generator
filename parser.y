%{
#include <cstdio>
#include <iostream>
using namespace std;

extern "C" int yylex();
extern "C" int yyparse();
extern "C" FILE *yyin;
 
void yyerror(const char *s);
%}
%union {
	// int ival;
	// float fval;
	// char *sval;
	char *adv_i;
	char *v_prs;
	char *adv_time;
	char *n_sing;
	char *adj_ino;
	char *pro;
	char *adj_cmpr;
	char *n_pl;
	char *delm;
	char *prev;
	char *v_pa;
	char *v_aux;
	char *adv_loc;
	char *v_imp;
	char *adj;
	char *adj_sup;
	char *adj_voc;
	char *unknown;
	char *adv_neg;
	char *det;
	char *sym;
	char *adv;
	char *v_sub;
	char *con;
	char *p;
	char *adv_comp;
	char *intt;
	char *v_pp;
	char *num;
	char *clitic;
	char *n_voc;
	char *fw;
	// char *badal;
	// char *motammam;
	// char *matoof;
	// char *sefat_pishvandi;
	// char *p;

}

// %token SNAZZLE TYPE
// %token END

// %token <sval> ADV_I
// %token <sval> V_PRS
// %token <sval> ADV_TIME
// %token <sval> N_SING
// %token <sval> ADJ_INO
// %token <sval> PRO
// %token <sval> ADJ_CMPR
// %token <sval> N_PL
// %token <sval> DELM
// %token <sval> PREV
// %token <sval> V_PA
// %token <sval> V_AUX
// %token <sval> ADV_LOC
// %token <sval> V_IMP
// %token <sval> ADJ
// %token <sval> ADJ_SUP
// %token <sval> ADJ_VOC
// %token <sval> unknown
// %token <sval> ADV_NEG
// %token <sval> DET
// %token <sval> SYM
// %token <sval> ADV
// %token <sval> V_SUB
// %token <sval> CON
// %token <sval> P
// %token <sval> ADV_COMP
// %token <sval> INT
// %token <sval> V_PP
// %token <sval> NUM
// %token <sval> CLITIC
// %token <sval> N_VOC
// %token <sval> FW
// %token <sval> badal
// %token <sval> motammam
// %token <sval> matoof
// %token <sval> sefat_pishvandi
// %token <sval> P
%token <adv_i> ADV_I
%token <v_prs> V_PRS
%token <adv_time> ADV_TIME
%token <n_sing> N_SING
%token <adj_ino> ADJ_INO
%token <pro> PRO
%token <adj_cmpr> ADJ_CMPR
%token <n_pl> N_PL
%token <delm> DELM
%token <prev> PREV
%token <v_pa> V_PA
%token <v_aux> V_AUX
%token <adv_loc> ADV_LOC
%token <v_imp> V_IMP
%token <adj> ADJ
%token <adj_sup> ADJ_SUP
%token <adj_voc> ADJ_VOC
%token <unknown> unknown
%token <adv_neg> ADV_NEG
%token <det> DET
%token <sym> SYM
%token <adv> ADV
%token <v_sub> V_SUB
%token <con> CON
%token <p> P
%token <adv_comp> ADV_COMP
%token <intt> INTT
%token <v_pp> V_PP
%token <num> NUM
%token <clitic> CLITIC
%token <n_voc> N_VOC
%token <fw> FW
// %token <badal> badal
// %token <motammam> motammam
// %token <matoof> matoof
// %token <sefat_pishvandi> sefat_pishvandi



%%

start: 
		jomle DELM {cout << "start -> jomle DELM\n";}
	|	jomle DELM start {cout << "start -> jomle DELM start\n";}
	;
jomle: 
		// fael gheid fel {cout << "jomle -> fael gheid fel\n";}
		CON jomle {cout << "jomle -> CON jomle, CON = " << $1 << endl;}
	|	nahad mosnad fel {cout << "jomle -> nahad mosnad fel\n";}
	// |	nahad P motammam fel {cout <<"jomle -> nahad P motammam fel, P = " << $2 << endl;}
	|	monada DELM jomle {cout << "jomle -> monada DELM jomle, DELM = " << $2 << endl;}
	;
esm: 
		N_SING {cout<<"esm -> N_SING, N_SING = "<< $1 << endl;}
	|	N_PL {cout <<"esm -> N_PL, N_PL = " << $1 << endl;}
	;
fel:
		V_AUX fel {cout << "fel -> V_AUX fel, V_AUX = " << $1 << endl;}
	|	V_PA {cout << "fel -> V_PA , V_PA = " << $1 << endl;}
	|	V_PP {cout << "fel -> V_PP , V_PP = " << $1 << endl;}
	|	V_PRS {cout << "fel -> V_PRS , V_PRS = " << $1 << endl;}
	|	V_SUB {cout << "fel -> V_SUB , V_SUB = " << $1 << endl;}
	|	V_IMP {cout << "fel -> V_IMP , V_IMP = " << $1 << endl;}
	; 
monada:
		N_VOC {cout << "monada -> N_VOC, N_VOC = " << $1 <<endl;}
	;
nahad:
	// 	esm S {cout << "nahad -> esm S\n";} 
	// | 	PRO S {cout << "nahad -> PRO S, PRO = " << $1 << endl;}
		esm {cout << "nahad -> esm\n";} 
	| 	PRO {cout << "nahad -> PRO, PRO = " << $1 << endl;}
	;
// S:
// 		vasf {cout << "S -> vasf.\n";} 
// 	| 	vasf vasf {cout << "S -> vasf vasf.\n";} 
// 	| 	vasf vasf vasf{cout << "S -> vasf vasf vasf.\n";} 
// 	| 	vasf vasf vasf vasf{cout << "S -> vasf vasf vasf vasf.\n";} 
// 	| 	vasf vasf vasf vasf vasf{cout << "S -> vasf vasf vasf vasf vasf.\n";}
	;
mosnad:
		sefatpishvandi sefat {cout << "mosnad -> sefatpishvandi sefat\n";}
	|	sefat {cout << "mosnad -> sefat\n";}
	|	esm {cout << "mosnad -> esm\n";}
	|	esm sefat {cout << "mosnad -> esm sefat\n";}
	|	sefatpishvandi esm sefat {cout << "mosnad -> sefatpishvandi esm sefat\n";}
	;
gheid: 
		P esm gheid {cout << "gheid -> P esm gheid, P = " << $1 << endl;}
	|	P {cout << "gheid -> P, P = " << $1 << endl;}
	|	ADV {cout << "gheid -> ADV, ADV = " << $1 << endl;}
	|	ADV_TIME {cout << "gheid -> ADV_TIME, ADV_TIME = " << $1 << endl;}
	;
sefat: 
		ADJ sefat {cout << "sefat -> ADJ sefat, ADJ = " << $1 << endl;}
	|	ADJ {cout << "sefat -> ADJ, ADJ = " << $1 << endl;}
	|	ADJ_CMPR {cout << "sefat -> ADJ_CMPR, ADJ_CMPR = " << $1 << endl;}
	|	ADJ_CMPR CON sefat {cout << "sefat -> ADJ_CMPR CON sefat, ADJ_CMPR = " << $1 << " CON = " << $2 << endl;}
	|	ADJ_CMPR sefat {cout << "sefat -> ADJ_CMPR sefat, ADJ_CMPR = " << $1 << endl;}
	|	gheid sefat {cout << "sefat -> gheid sefat\n";}
	;
sefatpishvandi:
		NUM sefatpishvandi {cout << "sefatpishvandi -> NUM sefatpishvandi, NUM = " << $1 << endl;}
	// |	ADJ_SUP sefat_pishvandi {cout << "sefatpishvandi -> ADJ_SUP sefat_pishvandi, ADJ_SUP = " << $1 << endl;}
	|	NUM {cout << "sefatpishvandi -> NUM, NUM = " << $1 << endl;}
	|	ADJ_SUP {cout << "sefatpishvandi -> ADJ_SUP, ADJ_SUP = " << $1 << endl;}
	;
// fael:
// 		esm S {cout << "fael -> esm S\n";}
// 	|	PRO S {cout << "fael -> PRO S, PRO = " << $1 << endl;}
// 	|	esm {cout << "fael -> esm.\n";}
// 	|	PRO {cout << "fael -> PRO, PRO = " << $1 << endl;}
// 	;
// maful:
// 		esm S {cout << "maful -> esm S\n";}
// 	|	PRO S {cout << "maful -> PRO S, PRO = " << $1 << endl;}
// 	;
// mozaf-elayh:
// 		esm S {cout << "mozaf-elayh -> esm S\n";}
// 	|	PRO S {cout << "mozaf-elayh -> PRO S, PRO = " << $1 << endl;}
// 	|	esm {cout << "mozaf-elayh -> esm.\n";}
// 	|	PRO {cout << "mozaf-elayh -> PRO, PRO = " << $1 << endl;}
// 	;
// vasf:
// 		sefat {cout << "vasf -> sefat\n";}
// 	|	mozaf-elayh {cout << "vasf -> mozaf-elayh\n";}
// 	// |	DELM badal {cout << "vasf -> DELM badal, DELM = " << $1 << endl;}
// 	// |	CON matoof {cout << "vasf -> CON matoof, CON = " << $1 << endl;}
	// ;

%%

int main(int argc, char** argv) {
	FILE *myfile = fopen(argv[1], "r");
	if (!myfile) {
		cout << "I can't open input file!" << endl;
		return -1;
	}	yyin = myfile;
	do {
		yyparse();
	} while (!feof(yyin));
	
}

void yyerror(const char *s) {
	cout << "Parse error!  Message: " << s << endl;
	// might as well halt now:
	// exit(-1);
}
