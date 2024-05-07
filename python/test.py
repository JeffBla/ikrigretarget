import sys, os
import ikrigretarget as ir


def config_gpt_meta():

    config = ir.SoulIKRigRetargetConfig()

    config.SourceCoord = ir.CoordType.RightHandYupZfront
    config.WorkCoord = ir.CoordType.RightHandYupZfront
    config.TargetCoord = ir.CoordType.RightHandYupZfront

    config.SourceRootType = ir.ERootType.RootZMinusGroundZ
    config.TargetRootType = ir.ERootType.RootZ

    config.SourceRootBone = "hip"
    config.SourceGroundBone = "lFoot"
    config.TargetRootBone = "Hips"
    config.TargetGroundBone = "LeftFoot"

    ### source chain
    # name         start                 end
    config.SourceChains = [
        ir.SoulIKRigChain("spine", "abdomen", "chest"),
        ir.SoulIKRigChain("head", "neck", "head"),

        # lleg
        ir.SoulIKRigChain("lleg", "lThigh", "lFoot"),

        # rleg
        ir.SoulIKRigChain("rleg", "rThigh", "rFoot"),

        # larm
        ir.SoulIKRigChain("larm", "lCollar", "lHand"),

        # rarm
        ir.SoulIKRigChain("rarm", "rCollar", "rHand"),
    ]

    ### target chain
    config.TargetChains.append(
        ir.SoulIKRigChain("spine", "LowerBack", "Spine1"))
    config.TargetChains.append(ir.SoulIKRigChain("head", "Neck", "Head"))

    # lleg
    config.TargetChains.append(
        ir.SoulIKRigChain("lleg", "LeftUpLeg", "LeftFoot"))

    # rleg
    config.TargetChains.append(
        ir.SoulIKRigChain("rleg", "RightUpLeg", "RightFoot"))

    # larm
    config.TargetChains.append(
        ir.SoulIKRigChain("larm", "LeftShoulder", "LeftHand"))

    # rarm
    config.TargetChains.append(
        ir.SoulIKRigChain("rarm", "RightShoulder", "RightHand"))

    ### chain mapping
    config.ChainMapping.append(
        ir.SoulIKRigChainMapping(True, False, "spine", "spine"))
    config.ChainMapping.append(
        ir.SoulIKRigChainMapping(True, False, "head", "head"))

    # lleg
    config.ChainMapping.append(
        ir.SoulIKRigChainMapping(True, False, "lleg", "lleg"))

    # rleg
    config.ChainMapping.append(
        ir.SoulIKRigChainMapping(True, False, "rleg", "rleg"))

    # larm
    config.ChainMapping.append(
        ir.SoulIKRigChainMapping(True, False, "larm", "larm"))

    # rarm
    config.ChainMapping.append(
        ir.SoulIKRigChainMapping(True, False, "rarm", "rarm"))

    return config


def test():

    a = ir.CoordType.RightHandZupYfront
    print("a:", a)

    config = ir.SoulIKRigRetargetConfig()

    # source chain
    config.SourceChains.append(ir.SoulIKRigChain("name0", "start0", "end1"))
    config.SourceChains.append(ir.SoulIKRigChain("name1", "start1", "end1"))

    # target chain
    config.TargetChains = [
        ir.SoulIKRigChain("name0", "start0", "end1"),
        ir.SoulIKRigChain("name1", "start1", "end1")
    ]

    # int array
    config.IntArray.append(1)
    config.IntArray = [1, 2, 3]

    print(config)

    print("IntArray:", len(config.IntArray))
    for i in config.IntArray:
        print(i)


def get_model_path():
    curdir = os.path.dirname(os.path.abspath(__file__))
    curdir = os.path.join(curdir, "..", "model")
    return curdir


def to_model_path(filename):
    return os.path.join(get_model_path(), filename)


if __name__ == "__main__":

    config = config_gpt_meta()
    print(config)

    srcAnimationFile = to_model_path("mMotion.fbx")
    srcTPoseFile = to_model_path("MocapNetTpose.fbx")
    targetFile = to_model_path("cmu__human_texture_noLeftBone.fbx")
    targetTPoseFile = to_model_path("cmu__human_texture_noLeftBone.fbx")
    outFile = to_model_path("out.fbx")

    ret = ir.retargetFBX(srcAnimationFile, srcTPoseFile, config.SourceRootBone,
                         targetFile, targetTPoseFile, outFile, config)
    print(ret)
