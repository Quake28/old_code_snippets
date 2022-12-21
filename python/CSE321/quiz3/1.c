Boolean blocked [2];
int turn;
void enter_critical_section(int process_id)
{
    blocked (process_id] = true;
    while(turn != id) {
        while(blocked[l - process_id])
    }
    turn=id;
}
void leave critical_section(int process_id)
{
    blocked[id] = false;
}