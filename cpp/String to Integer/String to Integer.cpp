struct numeric_only: std::ctype<char>
{
numeric_only(): std::ctype<char>(get­_table()) {}

static std::ctype_base::mas­k const* get_table()
{
static std::vector<std::cty­pe_base::mask>
rc(std::ctype<char>:­:table_size,std::cty­pe_base::space);

std::fill(&rc['0'], &rc[':'], std::ctype_base::dig­it);
return &rc[0];
}
};
