import wilson_wrapper.beta_wrapper as wp
import wilson.run.smeft.beta as betamodule

def test_configure_patch_sets_globals():
    wp.configure_patch("lq1_1221", 0.5)
    assert wp.key_var == "lq1_1221"
    assert wp.new_value == 0.5

def test_beta_function_is_patched_correctly():
    wp.configure_patch("lq1_1221", 0.5)

    # Sample input dict with the key that will be modified
    C_input = {"lq1_1221": 1.0}
    
    result = betamodule.beta(C_input)

    assert "lq1_1221" in result
    assert result["lq1_1221"] == 0.5

def test_unmodified_keys_remain():
    wp.configure_patch("lq1_1221", 0.5)

    # Include an additional key that shouldn't be touched
    C_input = {"lq1_1221": 1.0, "lq3_3333": 2.0}

    result = betamodule.beta(C_input)

    assert result["lq1_1221"] == 0.5
    assert result["lq3_3333"] == 2.0  # Assuming original beta returns same value
