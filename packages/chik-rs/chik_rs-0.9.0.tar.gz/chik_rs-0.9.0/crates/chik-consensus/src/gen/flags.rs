use klvmr::MEMPOOL_MODE as KLVM_MEMPOOL_MODE;

// flags controlling to condition parsing

// unknown condition codes are disallowed
pub const NO_UNKNOWN_CONDS: u32 = 0x20000;

// some conditions require an exact number of arguments (AGG_SIG_UNSAFE and
// AGG_SIG_ME). This will require those argument lists to be correctly
// nil-terminated
pub const COND_ARGS_NIL: u32 = 0x40000;

// With this flag, conditions will require the exact number of arguments
// currently supported for those conditions. This is meant for mempool-mode
pub const STRICT_ARGS_COUNT: u32 = 0x80000;

// disallow relative height- and time conditions on ephemeral spends
pub const NO_RELATIVE_CONDITIONS_ON_EPHEMERAL: u32 = 0x200000;

// enable softfork condition. Enabling this flag is a hard fork
pub const ENABLE_SOFTFORK_CONDITION: u32 = 0x400000;

// this lifts the restriction that AGG_SIG_ME and AGG_SIG_UNSAFE are only
// allowed to have two arguments. This makes the AGG_SIG_* conditions behave
// normal, just like all other conditions. Setting this flag is a hard fork
pub const AGG_SIG_ARGS: u32 = 0x800000;

// when this flag is set, the block generator serialization is allowed to
// contain back-references
pub const ALLOW_BACKREFS: u32 = 0x2000000;

// When set, the "flags" field of the Spend objects will be set depending on
// what features are detected of the spends
pub const ANALYZE_SPENDS: u32 = 0x4000000;

// This enables support for the new SEND_MESSAGE and RECEIVE_MESSAGE conditions
pub const ENABLE_MESSAGE_CONDITIONS: u32 = 0x8000000;

// When this flag is set, we reject AGG_SIG_* conditions whose public key is the
// infinity G1 point. Such public keys are mathematically valid, but do not
// provide any security guarantees. Chik has historically allowed them. Enabling
// this flag is a soft-fork.
pub const DISALLOW_INFINITY_G1: u32 = 0x10000000;

pub const MEMPOOL_MODE: u32 = KLVM_MEMPOOL_MODE
    | NO_UNKNOWN_CONDS
    | COND_ARGS_NIL
    | STRICT_ARGS_COUNT
    | NO_RELATIVE_CONDITIONS_ON_EPHEMERAL
    | ANALYZE_SPENDS
    | ENABLE_MESSAGE_CONDITIONS
    | DISALLOW_INFINITY_G1;
