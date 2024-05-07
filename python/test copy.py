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
        ir.SoulIKRigChain("lleg1", "lThigh", "lThigh"),
        ir.SoulIKRigChain("lleg2", "lShin", "lShin"),
        ir.SoulIKRigChain("lleg3", "lFoot", "lFoot"),

        # rleg
        ir.SoulIKRigChain("rleg1", "rThigh", "rThigh"),
        ir.SoulIKRigChain("rleg2", "rShin", "rShin"),
        ir.SoulIKRigChain("rleg3", "rFoot", "rFoot"),

        # larm
        ir.SoulIKRigChain("larm0", "lCollar", "lCollar"),
        ir.SoulIKRigChain("larm1", "lShldr", "lShldr"),
        ir.SoulIKRigChain("larm2", "lForeArm", "lForeArm"),
        ir.SoulIKRigChain("larm3", "lHand", "lHand"),

        # rarm
        ir.SoulIKRigChain("rarm0", "rCollar", "rCollar"),
        ir.SoulIKRigChain("rarm1", "rShldr", "rShldr"),
        ir.SoulIKRigChain("rarm2", "rForeArm", "rForeArm"),
        ir.SoulIKRigChain("rarm3", "rHand", "rHand"),
    ]

    ### target chain
    config.TargetChains.append(
        ir.SoulIKRigChain("spine", "LowerBack", "Spine1"))
    config.TargetChains.append(ir.SoulIKRigChain("head", "Neck", "Head"))

    # lleg
    config.TargetChains.append(
        ir.SoulIKRigChain("lleg1", "LeftUpLeg", "LeftUpLeg"))
    config.TargetChains.append(ir.SoulIKRigChain("lleg2", "LeftLeg",
                                                 "LeftLeg"))
    config.TargetChains.append(
        ir.SoulIKRigChain("lleg3", "LeftFoot", "LeftFoot"))

    # rleg
    config.TargetChains.append(
        ir.SoulIKRigChain("rleg1", "RightUpLeg", "RightUpLeg"))
    config.TargetChains.append(
        ir.SoulIKRigChain("rleg2", "RightLeg", "RightLeg"))
    config.TargetChains.append(
        ir.SoulIKRigChain("rleg3", "RightFoot", "RightFoot"))

    # larm
    config.TargetChains.append(
        ir.SoulIKRigChain("larm0", "LeftShoulder", "LeftShoulder"))
    config.TargetChains.append(ir.SoulIKRigChain("larm1", "LeftArm",
                                                 "LeftArm"))
    config.TargetChains.append(
        ir.SoulIKRigChain("larm2", "LeftForeArm", "LeftForeArm"))
    config.TargetChains.append(
        ir.SoulIKRigChain("larm3", "LeftHand", "LeftHand"))

    # rarm
    config.TargetChains.append(
        ir.SoulIKRigChain("rarm0", "RightShoulder", "RightShoulder"))
    config.TargetChains.append(
        ir.SoulIKRigChain("rarm1", "RightArm", "RightArm"))
    config.TargetChains.append(
        ir.SoulIKRigChain("rarm2", "RightForeArm", "RightForeArm"))
    config.TargetChains.append(
        ir.SoulIKRigChain("rarm3", "RightHand", "RightHand"))

    ### chain mapping
    config.ChainMapping.append(
        ir.SoulIKRigChainMapping(True, False, "spine", "spine"))
    config.ChainMapping.append(
        ir.SoulIKRigChainMapping(True, False, "head", "head"))

    # lleg
    config.ChainMapping.append(
        ir.SoulIKRigChainMapping(True, False, "lleg1", "lleg1"))
    config.ChainMapping.append(
        ir.SoulIKRigChainMapping(True, False, "lleg2", "lleg2"))
    config.ChainMapping.append(
        ir.SoulIKRigChainMapping(True, False, "lleg3", "lleg3"))

    # rleg
    config.ChainMapping.append(
        ir.SoulIKRigChainMapping(True, False, "rleg1", "rleg1"))
    config.ChainMapping.append(
        ir.SoulIKRigChainMapping(True, False, "rleg2", "rleg2"))
    config.ChainMapping.append(
        ir.SoulIKRigChainMapping(True, False, "rleg3", "rleg3"))

    # larm
    # config.ChainMapping.append(
    #     ir.SoulIKRigChainMapping(True, False, "larm0", "larm0"))
    config.ChainMapping.append(
        ir.SoulIKRigChainMapping(True, True, "larm1", "larm1"))
    config.ChainMapping.append(
        ir.SoulIKRigChainMapping(True, True, "larm2", "larm2"))
    config.ChainMapping.append(
        ir.SoulIKRigChainMapping(True, True, "larm3", "larm3"))

    # rarm
    config.ChainMapping.append(
        ir.SoulIKRigChainMapping(True, False, "rarm0", "rarm0"))
    config.ChainMapping.append(
        ir.SoulIKRigChainMapping(True, False, "rarm1", "rarm1"))
    config.ChainMapping.append(
        ir.SoulIKRigChainMapping(True, False, "rarm2", "rarm2"))
    config.ChainMapping.append(
        ir.SoulIKRigChainMapping(True, False, "rarm3", "rarm3"))

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
    targetFile = to_model_path("cmu_withTexture.fbx")
    targetTPoseFile = to_model_path("cmu_withTexture.fbx")
    outFile = to_model_path("out.fbx")

    ret = ir.retargetFBX(srcAnimationFile, srcTPoseFile, config.SourceRootBone,
                         targetFile, targetTPoseFile, outFile, config)
    print(ret)
