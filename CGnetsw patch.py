patchcode = bytes.fromhex("31 C0 90 90 90 90 90 90")

ea = get_inf_attr(INF_MIN_EA) 
end = get_inf_attr(INF_MAX_EA)
while(ea < end):
    if 'DeleteIp' in generate_disasm_line(ea, GENDSM_FORCE_CODE):
        # find call DeleteIp
        if 'sub' in print_insn_mnem(next_head(ea)) and 'esp' in print_operand(next_head(ea), 0):
            print(f"patched {ea} correct!")
            for i in range(8):
                ida_bytes.patch_byte(ea, patchcode[i])
                ea += 1
        ea = next_head(ea)
    else:
        ea = next_head(ea)
        
print("patch done!")
