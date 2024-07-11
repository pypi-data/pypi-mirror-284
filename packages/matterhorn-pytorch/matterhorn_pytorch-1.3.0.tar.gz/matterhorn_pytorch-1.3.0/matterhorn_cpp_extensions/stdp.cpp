#ifndef _MATTERHORN_STDP
#define _MATTERHORN_STDP


#include "stdp.h"
#include <ATen/ATen.h>
#include <ATen/Functions.h>
#include <cmath>
#include <iostream>
#include <vector>

using namespace std;

/*
STDP主函数。
Args:
    weight_mat (at::Tensor): 待更新的权重矩阵，形状为[output_shape,input_shape]
    input_shape (int): 输入向量长度
    output_shape (int): 输出向量长度
    time_steps (int): 时间步长
    input_spike_train (at::Tensor): 输入脉冲序列，形状为[time_steps,input_shape]
    output_spike_train (at::Tensor):
输出脉冲序列，形状为[time_steps,output_shape] a_pos (float): STDP参数$A^{+}$
    tau_pos (float): STDP参数$τ^{+}$
    a_neg (float): STDP参数$A^{-}$
    tau_neg (float): STDP参数$τ_{-}$
*/
void stdp(at::Tensor weight_mat,
          int input_shape,
          int output_shape,
          int time_steps,
          at::Tensor input_spike_train,
          at::Tensor output_spike_train,
          float a_pos,
          float tau_pos,
          float a_neg,
          float tau_neg,
          int batch_size = 1) {
    for (int i = 0; i < output_shape; i++) {
        for (int j = 0; j < input_shape; j++) {
            // 去遍历时间，更新权重
            at::Tensor weight = weight_mat[i][j];
            for (int b = 0; b < batch_size; b++) {
                // 遍历输出脉冲
                for (int ti = 0; ti < time_steps; ti++) {
                    at::Tensor spike_i = output_spike_train[ti][b][i];
                    if (spike_i.data<float>()[0] < 0.5f) {
                        continue;
                    }
                    // 遍历输入脉冲
                    for (int tj = 0; tj < time_steps; tj++) {
                        at::Tensor spike_j = input_spike_train[tj][b][j];
                        if (spike_j.data<float>()[0] < 0.5f) {
                            continue;
                        }
                        float dt = (float)(ti - tj);
                        if (dt > 0.0f) {
                            weight += a_pos * powf(1.0f / tau_pos, dt - 1.0f);
                        } else if (dt < 0.0f) {
                            weight -= a_neg * powf(1.0f / tau_neg, -dt - 1.0f);
                        }
                    }
                }
            }
        }
    }
}


#endif