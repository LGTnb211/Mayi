import numpy as np
import math
def distance(point1, point2):
    # 计算两个点之间的欧几里德距离
    return np.linalg.norm(point1 - point2)

def objective_function():

    return
def downhill_simplex_method(guding_dian, start_points, alpha=1, beta=0.5, gamma=2, epsilon=0.1):
    n = 3
    sorted_simplex = np.array(start_points, dtype=float)
    all_last_point = []
    # count = 0  # 计数器
    # prev_obj_func_value = float('inf')  # 上一次的目标函数值
    while True:
        # 计算各顶点的函数值
        values = []
        for i in range(len(sorted_simplex)):
            values.append(objective_function(point1=guding_dian, point2=(sorted_simplex[i])))
        # values = [objective_function(*point) for point in sorted_simplex]
        # 对顶点进行排序
        sorted_indices = np.argsort(values)
        sorted_simplex = sorted_simplex[sorted_indices]
        # 计算重心
        centroid = np.mean(sorted_simplex[:-1], axis=0)
        # 计算反射点
        reflection_point = centroid + alpha * (centroid - sorted_simplex[-1])
        reflection_value = objective_function(point1=guding_dian, point2=reflection_point)
        print("reflection_value: {}".format(reflection_value))

        if reflection_value < values[sorted_indices[0]]:
            # 找到更好的解，尝试扩展
            expansion_point = centroid + gamma * (reflection_point - centroid)
            expansion_value = objective_function(point1=guding_dian, point2=expansion_point)
            print("expansion_value: {}".format(expansion_value))
            if expansion_value < reflection_value:
                sorted_simplex[-1] = expansion_point
            else:
                sorted_simplex[-1] = reflection_point
        else:
            if reflection_value < values[sorted_indices[-2]]:
                # 替换最差的点
                sorted_simplex[-1] = reflection_point
            else:
                # 进行收缩操作
                contraction_point = centroid + beta * (sorted_simplex[-1] - centroid)
                contraction_value = objective_function(guding_dian, contraction_point)

                if contraction_value < values[sorted_indices[-1]]:
                    sorted_simplex[-1] = contraction_point
                else:
                    # 缩小整个单纯形
                    for i in range(1, n + 1):
                        sorted_simplex[i] = sorted_simplex[0] + 0.5 * (sorted_simplex[i] - sorted_simplex[0])
        all_last_point.append(sorted_simplex[-1])
        # 判断终止条件
        # if objective_function(guding_dian, sorted_simplex[-1]) < epsilon:
        #     return sorted_simplex[-1], all_last_point, objective_function(guding_dian, sorted_simplex[-1])
        # elif objective_function(guding_dian, sorted_simplex[-1]) == prev_obj_func_value:
        #     count += 1
        #     if count == 5:
        #         return sorted_simplex[-1], all_last_point, objective_function(guding_dian, sorted_simplex[-1])
        # else:
        #     count = 0
        # prev_obj_func_value = objective_function(guding_dian, sorted_simplex[-1])
        # print("终止条件未满足，继续循环")
        # print("sorted_simple:\n{}".format(sorted_simplex))
        if distance(sorted_simplex[0], sorted_simplex[-1]) < epsilon:
            return sorted_simplex[-1], all_last_point, objective_function(guding_dian, sorted_simplex[-1])
        #else:
            #print("终止条件为满足，继续循环")
            # print("sorted_simple:\n{}".format(sorted_simplex))