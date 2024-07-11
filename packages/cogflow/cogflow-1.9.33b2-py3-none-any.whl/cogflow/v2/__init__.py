from kfp import v2 as kfp_v2

# Import everything from kfp.v2 into the cogflow.v2 namespace
globals().update(vars(kfp_v2))