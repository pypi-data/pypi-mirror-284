/**
  ******************************************************************************
  * @file    network.c
  * @author  AST Embedded Analytics Research Platform
  * @date    Tue May 21 19:17:52 2024
  * @brief   AI Tool Automatic Code Generator for Embedded NN computing
  ******************************************************************************
  * @attention
  *
  * Copyright (c) 2018 STMicroelectronics.
  * All rights reserved.
  *
  * This software component is licensed by ST under Ultimate Liberty license
  * SLA0044, the "License"; You may not use this file except in compliance with
  * the License. You may obtain a copy of the License at:
  *                             www.st.com/SLA0044
  *
  ******************************************************************************
  */


#include "network.h"

#include "ai_platform_interface.h"
#include "ai_math_helpers.h"

#include "core_common.h"
#include "layers.h"



#undef AI_TOOLS_VERSION_MAJOR
#undef AI_TOOLS_VERSION_MINOR
#undef AI_TOOLS_VERSION_MICRO
#define AI_TOOLS_VERSION_MAJOR 5
#define AI_TOOLS_VERSION_MINOR 2
#define AI_TOOLS_VERSION_MICRO 0


#undef AI_TOOLS_API_VERSION_MAJOR
#undef AI_TOOLS_API_VERSION_MINOR
#undef AI_TOOLS_API_VERSION_MICRO
#define AI_TOOLS_API_VERSION_MAJOR 1
#define AI_TOOLS_API_VERSION_MINOR 3
#define AI_TOOLS_API_VERSION_MICRO 0

#undef AI_NET_OBJ_INSTANCE
#define AI_NET_OBJ_INSTANCE g_network
 
#undef AI_NETWORK_MODEL_SIGNATURE
#define AI_NETWORK_MODEL_SIGNATURE     "c512936526370e16350bb20859d13c63"

#ifndef AI_TOOLS_REVISION_ID
#define AI_TOOLS_REVISION_ID     "(rev-5.2.0)"
#endif

#undef AI_TOOLS_DATE_TIME
#define AI_TOOLS_DATE_TIME   "Tue May 21 19:17:52 2024"

#undef AI_TOOLS_COMPILE_TIME
#define AI_TOOLS_COMPILE_TIME    __DATE__ " " __TIME__

#undef AI_NETWORK_N_BATCHES
#define AI_NETWORK_N_BATCHES         (1)

/**  Forward network declaration section  *************************************/
AI_STATIC ai_network AI_NET_OBJ_INSTANCE;


/**  Forward network array declarations  **************************************/
AI_STATIC ai_array conv2d_34_scratch0_array;   /* Array #0 */
AI_STATIC ai_array conv2d_29_scratch0_array;   /* Array #1 */
AI_STATIC ai_array conv2d_23_scratch0_array;   /* Array #2 */
AI_STATIC ai_array conv2d_10_scratch0_array;   /* Array #3 */
AI_STATIC ai_array conv2d_9_scratch0_array;   /* Array #4 */
AI_STATIC ai_array conv2d_3_scratch0_array;   /* Array #5 */
AI_STATIC ai_array dense_40_bias_array;   /* Array #6 */
AI_STATIC ai_array dense_40_weights_array;   /* Array #7 */
AI_STATIC ai_array tflpseudo_qconst2_array;   /* Array #8 */
AI_STATIC ai_array conv2d_34_bias_array;   /* Array #9 */
AI_STATIC ai_array conv2d_34_weights_array;   /* Array #10 */
AI_STATIC ai_array tflpseudo_qconst4_array;   /* Array #11 */
AI_STATIC ai_array conv2d_29_bias_array;   /* Array #12 */
AI_STATIC ai_array conv2d_29_weights_array;   /* Array #13 */
AI_STATIC ai_array tflpseudo_qconst6_array;   /* Array #14 */
AI_STATIC ai_array conv2d_23_bias_array;   /* Array #15 */
AI_STATIC ai_array conv2d_23_weights_array;   /* Array #16 */
AI_STATIC ai_array tflpseudo_qconst8_array;   /* Array #17 */
AI_STATIC ai_array tflpseudo_qconst9_array;   /* Array #18 */
AI_STATIC ai_array conv2d_10_bias_array;   /* Array #19 */
AI_STATIC ai_array conv2d_10_weights_array;   /* Array #20 */
AI_STATIC ai_array conv2d_9_bias_array;   /* Array #21 */
AI_STATIC ai_array conv2d_9_weights_array;   /* Array #22 */
AI_STATIC ai_array tflpseudo_qconst12_array;   /* Array #23 */
AI_STATIC ai_array conv2d_3_bias_array;   /* Array #24 */
AI_STATIC ai_array conv2d_3_weights_array;   /* Array #25 */
AI_STATIC ai_array inputs_output_array;   /* Array #26 */
AI_STATIC ai_array conversion_0_output_array;   /* Array #27 */
AI_STATIC ai_array pad_1_output_array;   /* Array #28 */
AI_STATIC ai_array conv2d_3_output_array;   /* Array #29 */
AI_STATIC ai_array eltwise_5_output_array;   /* Array #30 */
AI_STATIC ai_array conv2d_9_output_array;   /* Array #31 */
AI_STATIC ai_array eltwise_13_output_array;   /* Array #32 */
AI_STATIC ai_array pool_17_output_array;   /* Array #33 */
AI_STATIC ai_array pad_6_output_array;   /* Array #34 */
AI_STATIC ai_array conv2d_10_output_array;   /* Array #35 */
AI_STATIC ai_array eltwise_14_output_array;   /* Array #36 */
AI_STATIC ai_array pool_18_output_array;   /* Array #37 */
AI_STATIC ai_array nl_18_output_array;   /* Array #38 */
AI_STATIC ai_array pad_21_output_array;   /* Array #39 */
AI_STATIC ai_array conv2d_23_output_array;   /* Array #40 */
AI_STATIC ai_array eltwise_25_output_array;   /* Array #41 */
AI_STATIC ai_array eltwise_26_output_array;   /* Array #42 */
AI_STATIC ai_array pad_27_output_array;   /* Array #43 */
AI_STATIC ai_array conv2d_29_output_array;   /* Array #44 */
AI_STATIC ai_array eltwise_31_output_array;   /* Array #45 */
AI_STATIC ai_array pad_32_output_array;   /* Array #46 */
AI_STATIC ai_array conv2d_34_output_array;   /* Array #47 */
AI_STATIC ai_array eltwise_36_output_array;   /* Array #48 */
AI_STATIC ai_array eltwise_37_output_array;   /* Array #49 */
AI_STATIC ai_array pool_39_output_array;   /* Array #50 */
AI_STATIC ai_array dense_40_output_array;   /* Array #51 */
AI_STATIC ai_array conversion_41_output_array;   /* Array #52 */


/**  Forward network tensor declarations  *************************************/
AI_STATIC ai_tensor conv2d_34_scratch0;   /* Tensor #0 */
AI_STATIC ai_tensor conv2d_29_scratch0;   /* Tensor #1 */
AI_STATIC ai_tensor conv2d_23_scratch0;   /* Tensor #2 */
AI_STATIC ai_tensor conv2d_10_scratch0;   /* Tensor #3 */
AI_STATIC ai_tensor conv2d_9_scratch0;   /* Tensor #4 */
AI_STATIC ai_tensor conv2d_3_scratch0;   /* Tensor #5 */
AI_STATIC ai_tensor dense_40_bias;   /* Tensor #6 */
AI_STATIC ai_tensor dense_40_weights;   /* Tensor #7 */
AI_STATIC ai_tensor tflpseudo_qconst2;   /* Tensor #8 */
AI_STATIC ai_tensor conv2d_34_bias;   /* Tensor #9 */
AI_STATIC ai_tensor conv2d_34_weights;   /* Tensor #10 */
AI_STATIC ai_tensor tflpseudo_qconst4;   /* Tensor #11 */
AI_STATIC ai_tensor conv2d_29_bias;   /* Tensor #12 */
AI_STATIC ai_tensor conv2d_29_weights;   /* Tensor #13 */
AI_STATIC ai_tensor tflpseudo_qconst6;   /* Tensor #14 */
AI_STATIC ai_tensor conv2d_23_bias;   /* Tensor #15 */
AI_STATIC ai_tensor conv2d_23_weights;   /* Tensor #16 */
AI_STATIC ai_tensor tflpseudo_qconst8;   /* Tensor #17 */
AI_STATIC ai_tensor tflpseudo_qconst9;   /* Tensor #18 */
AI_STATIC ai_tensor conv2d_10_bias;   /* Tensor #19 */
AI_STATIC ai_tensor conv2d_10_weights;   /* Tensor #20 */
AI_STATIC ai_tensor conv2d_9_bias;   /* Tensor #21 */
AI_STATIC ai_tensor conv2d_9_weights;   /* Tensor #22 */
AI_STATIC ai_tensor tflpseudo_qconst12;   /* Tensor #23 */
AI_STATIC ai_tensor conv2d_3_bias;   /* Tensor #24 */
AI_STATIC ai_tensor conv2d_3_weights;   /* Tensor #25 */
AI_STATIC ai_tensor inputs_output;   /* Tensor #26 */
AI_STATIC ai_tensor conversion_0_output;   /* Tensor #27 */
AI_STATIC ai_tensor pad_1_output;   /* Tensor #28 */
AI_STATIC ai_tensor conv2d_3_output;   /* Tensor #29 */
AI_STATIC ai_tensor eltwise_5_output;   /* Tensor #30 */
AI_STATIC ai_tensor conv2d_9_output;   /* Tensor #31 */
AI_STATIC ai_tensor eltwise_13_output;   /* Tensor #32 */
AI_STATIC ai_tensor pool_17_output;   /* Tensor #33 */
AI_STATIC ai_tensor pad_6_output;   /* Tensor #34 */
AI_STATIC ai_tensor conv2d_10_output;   /* Tensor #35 */
AI_STATIC ai_tensor eltwise_14_output;   /* Tensor #36 */
AI_STATIC ai_tensor pool_18_output;   /* Tensor #37 */
AI_STATIC ai_tensor nl_18_output;   /* Tensor #38 */
AI_STATIC ai_tensor pad_21_output;   /* Tensor #39 */
AI_STATIC ai_tensor conv2d_23_output;   /* Tensor #40 */
AI_STATIC ai_tensor eltwise_25_output;   /* Tensor #41 */
AI_STATIC ai_tensor eltwise_26_output;   /* Tensor #42 */
AI_STATIC ai_tensor pad_27_output;   /* Tensor #43 */
AI_STATIC ai_tensor conv2d_29_output;   /* Tensor #44 */
AI_STATIC ai_tensor eltwise_31_output;   /* Tensor #45 */
AI_STATIC ai_tensor pad_32_output;   /* Tensor #46 */
AI_STATIC ai_tensor conv2d_34_output;   /* Tensor #47 */
AI_STATIC ai_tensor eltwise_36_output;   /* Tensor #48 */
AI_STATIC ai_tensor eltwise_37_output;   /* Tensor #49 */
AI_STATIC ai_tensor pool_39_output;   /* Tensor #50 */
AI_STATIC ai_tensor dense_40_output;   /* Tensor #51 */
AI_STATIC ai_tensor conversion_41_output;   /* Tensor #52 */


/**  Forward network tensor chain declarations  *******************************/
AI_STATIC_CONST ai_tensor_chain conversion_0_chain;   /* Chain #0 */
AI_STATIC_CONST ai_tensor_chain pad_1_chain;   /* Chain #1 */
AI_STATIC_CONST ai_tensor_chain conv2d_3_chain;   /* Chain #2 */
AI_STATIC_CONST ai_tensor_chain eltwise_5_chain;   /* Chain #3 */
AI_STATIC_CONST ai_tensor_chain conv2d_9_chain;   /* Chain #4 */
AI_STATIC_CONST ai_tensor_chain eltwise_13_chain;   /* Chain #5 */
AI_STATIC_CONST ai_tensor_chain pool_17_chain;   /* Chain #6 */
AI_STATIC_CONST ai_tensor_chain pad_6_chain;   /* Chain #7 */
AI_STATIC_CONST ai_tensor_chain conv2d_10_chain;   /* Chain #8 */
AI_STATIC_CONST ai_tensor_chain eltwise_14_chain;   /* Chain #9 */
AI_STATIC_CONST ai_tensor_chain pool_18_chain;   /* Chain #10 */
AI_STATIC_CONST ai_tensor_chain nl_18_chain;   /* Chain #11 */
AI_STATIC_CONST ai_tensor_chain pad_21_chain;   /* Chain #12 */
AI_STATIC_CONST ai_tensor_chain conv2d_23_chain;   /* Chain #13 */
AI_STATIC_CONST ai_tensor_chain eltwise_25_chain;   /* Chain #14 */
AI_STATIC_CONST ai_tensor_chain eltwise_26_chain;   /* Chain #15 */
AI_STATIC_CONST ai_tensor_chain pad_27_chain;   /* Chain #16 */
AI_STATIC_CONST ai_tensor_chain conv2d_29_chain;   /* Chain #17 */
AI_STATIC_CONST ai_tensor_chain eltwise_31_chain;   /* Chain #18 */
AI_STATIC_CONST ai_tensor_chain pad_32_chain;   /* Chain #19 */
AI_STATIC_CONST ai_tensor_chain conv2d_34_chain;   /* Chain #20 */
AI_STATIC_CONST ai_tensor_chain eltwise_36_chain;   /* Chain #21 */
AI_STATIC_CONST ai_tensor_chain eltwise_37_chain;   /* Chain #22 */
AI_STATIC_CONST ai_tensor_chain pool_39_chain;   /* Chain #23 */
AI_STATIC_CONST ai_tensor_chain dense_40_chain;   /* Chain #24 */
AI_STATIC_CONST ai_tensor_chain conversion_41_chain;   /* Chain #25 */


/**  Forward network layer declarations  **************************************/
AI_STATIC ai_layer_nl conversion_0_layer; /* Layer #0 */
AI_STATIC ai_layer_pad pad_1_layer; /* Layer #1 */
AI_STATIC ai_layer_conv2d conv2d_3_layer; /* Layer #2 */
AI_STATIC ai_layer_eltwise eltwise_5_layer; /* Layer #3 */
AI_STATIC ai_layer_conv2d conv2d_9_layer; /* Layer #4 */
AI_STATIC ai_layer_eltwise eltwise_13_layer; /* Layer #5 */
AI_STATIC ai_layer_pool pool_17_layer; /* Layer #6 */
AI_STATIC ai_layer_pad pad_6_layer; /* Layer #7 */
AI_STATIC ai_layer_conv2d conv2d_10_layer; /* Layer #8 */
AI_STATIC ai_layer_eltwise eltwise_14_layer; /* Layer #9 */
AI_STATIC ai_layer_pool pool_18_layer; /* Layer #10 */
AI_STATIC ai_layer_nl nl_18_layer; /* Layer #11 */
AI_STATIC ai_layer_pad pad_21_layer; /* Layer #12 */
AI_STATIC ai_layer_conv2d conv2d_23_layer; /* Layer #13 */
AI_STATIC ai_layer_eltwise eltwise_25_layer; /* Layer #14 */
AI_STATIC ai_layer_eltwise eltwise_26_layer; /* Layer #15 */
AI_STATIC ai_layer_pad pad_27_layer; /* Layer #16 */
AI_STATIC ai_layer_conv2d conv2d_29_layer; /* Layer #17 */
AI_STATIC ai_layer_eltwise eltwise_31_layer; /* Layer #18 */
AI_STATIC ai_layer_pad pad_32_layer; /* Layer #19 */
AI_STATIC ai_layer_conv2d conv2d_34_layer; /* Layer #20 */
AI_STATIC ai_layer_eltwise eltwise_36_layer; /* Layer #21 */
AI_STATIC ai_layer_eltwise eltwise_37_layer; /* Layer #22 */
AI_STATIC ai_layer_pool pool_39_layer; /* Layer #23 */
AI_STATIC ai_layer_dense dense_40_layer; /* Layer #24 */
AI_STATIC ai_layer_nl conversion_41_layer; /* Layer #25 */


/**  Array declarations section  **********************************************/
/* Array#0 */
AI_ARRAY_OBJ_DECLARE(
  conv2d_34_scratch0_array, AI_ARRAY_FORMAT_S8,
  NULL, NULL, 592, AI_STATIC)

/* Array#1 */
AI_ARRAY_OBJ_DECLARE(
  conv2d_29_scratch0_array, AI_ARRAY_FORMAT_S8,
  NULL, NULL, 592, AI_STATIC)

/* Array#2 */
AI_ARRAY_OBJ_DECLARE(
  conv2d_23_scratch0_array, AI_ARRAY_FORMAT_S8,
  NULL, NULL, 592, AI_STATIC)

/* Array#3 */
AI_ARRAY_OBJ_DECLARE(
  conv2d_10_scratch0_array, AI_ARRAY_FORMAT_S8,
  NULL, NULL, 592, AI_STATIC)

/* Array#4 */
AI_ARRAY_OBJ_DECLARE(
  conv2d_9_scratch0_array, AI_ARRAY_FORMAT_S8,
  NULL, NULL, 112, AI_STATIC)

/* Array#5 */
AI_ARRAY_OBJ_DECLARE(
  conv2d_3_scratch0_array, AI_ARRAY_FORMAT_S8,
  NULL, NULL, 652, AI_STATIC)

/* Array#6 */
AI_ARRAY_OBJ_DECLARE(
  dense_40_bias_array, AI_ARRAY_FORMAT_S32,
  NULL, NULL, 6, AI_STATIC)

/* Array#7 */
AI_ARRAY_OBJ_DECLARE(
  dense_40_weights_array, AI_ARRAY_FORMAT_S8,
  NULL, NULL, 48, AI_STATIC)

/* Array#8 */
AI_ARRAY_OBJ_DECLARE(
  tflpseudo_qconst2_array, AI_ARRAY_FORMAT_S8,
  NULL, NULL, 8, AI_STATIC)

/* Array#9 */
AI_ARRAY_OBJ_DECLARE(
  conv2d_34_bias_array, AI_ARRAY_FORMAT_S32,
  NULL, NULL, 8, AI_STATIC)

/* Array#10 */
AI_ARRAY_OBJ_DECLARE(
  conv2d_34_weights_array, AI_ARRAY_FORMAT_S8,
  NULL, NULL, 192, AI_STATIC)

/* Array#11 */
AI_ARRAY_OBJ_DECLARE(
  tflpseudo_qconst4_array, AI_ARRAY_FORMAT_S8,
  NULL, NULL, 8, AI_STATIC)

/* Array#12 */
AI_ARRAY_OBJ_DECLARE(
  conv2d_29_bias_array, AI_ARRAY_FORMAT_S32,
  NULL, NULL, 8, AI_STATIC)

/* Array#13 */
AI_ARRAY_OBJ_DECLARE(
  conv2d_29_weights_array, AI_ARRAY_FORMAT_S8,
  NULL, NULL, 192, AI_STATIC)

/* Array#14 */
AI_ARRAY_OBJ_DECLARE(
  tflpseudo_qconst6_array, AI_ARRAY_FORMAT_S8,
  NULL, NULL, 8, AI_STATIC)

/* Array#15 */
AI_ARRAY_OBJ_DECLARE(
  conv2d_23_bias_array, AI_ARRAY_FORMAT_S32,
  NULL, NULL, 8, AI_STATIC)

/* Array#16 */
AI_ARRAY_OBJ_DECLARE(
  conv2d_23_weights_array, AI_ARRAY_FORMAT_S8,
  NULL, NULL, 192, AI_STATIC)

/* Array#17 */
AI_ARRAY_OBJ_DECLARE(
  tflpseudo_qconst8_array, AI_ARRAY_FORMAT_S8,
  NULL, NULL, 8, AI_STATIC)

/* Array#18 */
AI_ARRAY_OBJ_DECLARE(
  tflpseudo_qconst9_array, AI_ARRAY_FORMAT_S8,
  NULL, NULL, 8, AI_STATIC)

/* Array#19 */
AI_ARRAY_OBJ_DECLARE(
  conv2d_10_bias_array, AI_ARRAY_FORMAT_S32,
  NULL, NULL, 8, AI_STATIC)

/* Array#20 */
AI_ARRAY_OBJ_DECLARE(
  conv2d_10_weights_array, AI_ARRAY_FORMAT_S8,
  NULL, NULL, 192, AI_STATIC)

/* Array#21 */
AI_ARRAY_OBJ_DECLARE(
  conv2d_9_bias_array, AI_ARRAY_FORMAT_S32,
  NULL, NULL, 8, AI_STATIC)

/* Array#22 */
AI_ARRAY_OBJ_DECLARE(
  conv2d_9_weights_array, AI_ARRAY_FORMAT_S8,
  NULL, NULL, 64, AI_STATIC)

/* Array#23 */
AI_ARRAY_OBJ_DECLARE(
  tflpseudo_qconst12_array, AI_ARRAY_FORMAT_S8,
  NULL, NULL, 8, AI_STATIC)

/* Array#24 */
AI_ARRAY_OBJ_DECLARE(
  conv2d_3_bias_array, AI_ARRAY_FORMAT_S32,
  NULL, NULL, 8, AI_STATIC)

/* Array#25 */
AI_ARRAY_OBJ_DECLARE(
  conv2d_3_weights_array, AI_ARRAY_FORMAT_S8,
  NULL, NULL, 216, AI_STATIC)

/* Array#26 */
AI_ARRAY_OBJ_DECLARE(
  inputs_output_array, AI_ARRAY_FORMAT_FLOAT|AI_FMT_FLAG_IS_IO,
  NULL, NULL, 1152, AI_STATIC)

/* Array#27 */
AI_ARRAY_OBJ_DECLARE(
  conversion_0_output_array, AI_ARRAY_FORMAT_S8,
  NULL, NULL, 1152, AI_STATIC)

/* Array#28 */
AI_ARRAY_OBJ_DECLARE(
  pad_1_output_array, AI_ARRAY_FORMAT_S8,
  NULL, NULL, 1170, AI_STATIC)

/* Array#29 */
AI_ARRAY_OBJ_DECLARE(
  conv2d_3_output_array, AI_ARRAY_FORMAT_S8,
  NULL, NULL, 1024, AI_STATIC)

/* Array#30 */
AI_ARRAY_OBJ_DECLARE(
  eltwise_5_output_array, AI_ARRAY_FORMAT_S8,
  NULL, NULL, 1024, AI_STATIC)

/* Array#31 */
AI_ARRAY_OBJ_DECLARE(
  conv2d_9_output_array, AI_ARRAY_FORMAT_S8,
  NULL, NULL, 1024, AI_STATIC)

/* Array#32 */
AI_ARRAY_OBJ_DECLARE(
  eltwise_13_output_array, AI_ARRAY_FORMAT_S8,
  NULL, NULL, 1024, AI_STATIC)

/* Array#33 */
AI_ARRAY_OBJ_DECLARE(
  pool_17_output_array, AI_ARRAY_FORMAT_S8,
  NULL, NULL, 512, AI_STATIC)

/* Array#34 */
AI_ARRAY_OBJ_DECLARE(
  pad_6_output_array, AI_ARRAY_FORMAT_S8,
  NULL, NULL, 1040, AI_STATIC)

/* Array#35 */
AI_ARRAY_OBJ_DECLARE(
  conv2d_10_output_array, AI_ARRAY_FORMAT_S8,
  NULL, NULL, 1024, AI_STATIC)

/* Array#36 */
AI_ARRAY_OBJ_DECLARE(
  eltwise_14_output_array, AI_ARRAY_FORMAT_S8,
  NULL, NULL, 1024, AI_STATIC)

/* Array#37 */
AI_ARRAY_OBJ_DECLARE(
  pool_18_output_array, AI_ARRAY_FORMAT_S8,
  NULL, NULL, 512, AI_STATIC)

/* Array#38 */
AI_ARRAY_OBJ_DECLARE(
  nl_18_output_array, AI_ARRAY_FORMAT_S8,
  NULL, NULL, 512, AI_STATIC)

/* Array#39 */
AI_ARRAY_OBJ_DECLARE(
  pad_21_output_array, AI_ARRAY_FORMAT_S8,
  NULL, NULL, 528, AI_STATIC)

/* Array#40 */
AI_ARRAY_OBJ_DECLARE(
  conv2d_23_output_array, AI_ARRAY_FORMAT_S8,
  NULL, NULL, 512, AI_STATIC)

/* Array#41 */
AI_ARRAY_OBJ_DECLARE(
  eltwise_25_output_array, AI_ARRAY_FORMAT_S8,
  NULL, NULL, 512, AI_STATIC)

/* Array#42 */
AI_ARRAY_OBJ_DECLARE(
  eltwise_26_output_array, AI_ARRAY_FORMAT_S8,
  NULL, NULL, 512, AI_STATIC)

/* Array#43 */
AI_ARRAY_OBJ_DECLARE(
  pad_27_output_array, AI_ARRAY_FORMAT_S8,
  NULL, NULL, 528, AI_STATIC)

/* Array#44 */
AI_ARRAY_OBJ_DECLARE(
  conv2d_29_output_array, AI_ARRAY_FORMAT_S8,
  NULL, NULL, 512, AI_STATIC)

/* Array#45 */
AI_ARRAY_OBJ_DECLARE(
  eltwise_31_output_array, AI_ARRAY_FORMAT_S8,
  NULL, NULL, 512, AI_STATIC)

/* Array#46 */
AI_ARRAY_OBJ_DECLARE(
  pad_32_output_array, AI_ARRAY_FORMAT_S8,
  NULL, NULL, 528, AI_STATIC)

/* Array#47 */
AI_ARRAY_OBJ_DECLARE(
  conv2d_34_output_array, AI_ARRAY_FORMAT_S8,
  NULL, NULL, 512, AI_STATIC)

/* Array#48 */
AI_ARRAY_OBJ_DECLARE(
  eltwise_36_output_array, AI_ARRAY_FORMAT_S8,
  NULL, NULL, 512, AI_STATIC)

/* Array#49 */
AI_ARRAY_OBJ_DECLARE(
  eltwise_37_output_array, AI_ARRAY_FORMAT_S8,
  NULL, NULL, 512, AI_STATIC)

/* Array#50 */
AI_ARRAY_OBJ_DECLARE(
  pool_39_output_array, AI_ARRAY_FORMAT_S8,
  NULL, NULL, 8, AI_STATIC)

/* Array#51 */
AI_ARRAY_OBJ_DECLARE(
  dense_40_output_array, AI_ARRAY_FORMAT_S8,
  NULL, NULL, 6, AI_STATIC)

/* Array#52 */
AI_ARRAY_OBJ_DECLARE(
  conversion_41_output_array, AI_ARRAY_FORMAT_FLOAT|AI_FMT_FLAG_IS_IO,
  NULL, NULL, 6, AI_STATIC)

/**  Array metadata declarations section  *************************************/
/* Int quant #0 */
AI_INTQ_INFO_LIST_OBJ_DECLARE(dense_40_bias_intq, AI_STATIC_CONST,
  AI_BUFFER_META_FLAG_SCALE_FLOAT|AI_BUFFER_META_FLAG_ZEROPOINT_S8, 1,
  AI_PACK_INTQ_INFO(
    AI_PACK_INTQ_SCALE(0.000589505594689399f),
    AI_PACK_INTQ_ZP(0)))

/* Int quant #1 */
AI_INTQ_INFO_LIST_OBJ_DECLARE(dense_40_weights_intq, AI_STATIC_CONST,
  AI_BUFFER_META_FLAG_SCALE_FLOAT|AI_BUFFER_META_FLAG_ZEROPOINT_S8, 1,
  AI_PACK_INTQ_INFO(
    AI_PACK_INTQ_SCALE(0.005759225692600012f),
    AI_PACK_INTQ_ZP(0)))

/* Int quant #2 */
AI_INTQ_INFO_LIST_OBJ_DECLARE(tflpseudo_qconst2_intq, AI_STATIC_CONST,
  AI_BUFFER_META_FLAG_SCALE_FLOAT|AI_BUFFER_META_FLAG_ZEROPOINT_S8, 1,
  AI_PACK_INTQ_INFO(
    AI_PACK_INTQ_SCALE(0.0038639686536043882f),
    AI_PACK_INTQ_ZP(-77)))

/* Int quant #3 */
AI_INTQ_INFO_LIST_OBJ_DECLARE(conv2d_34_bias_intq, AI_STATIC_CONST,
  AI_BUFFER_META_FLAG_SCALE_FLOAT|AI_BUFFER_META_FLAG_ZEROPOINT_S8, 8,
  AI_PACK_INTQ_INFO(
    AI_PACK_INTQ_SCALE(0.0003923600015696138f, 0.0004081027873326093f, 0.00022787073976360261f, 0.0005191720556467772f, 0.0003791704948525876f, 0.0005738171748816967f, 0.00039893004577606916f, 0.0004973643226549029f),
    AI_PACK_INTQ_ZP(0, 0, 0, 0, 0, 0, 0, 0)))

/* Int quant #4 */
AI_INTQ_INFO_LIST_OBJ_DECLARE(conv2d_34_weights_intq, AI_STATIC_CONST,
  AI_BUFFER_META_FLAG_SCALE_FLOAT|AI_BUFFER_META_FLAG_ZEROPOINT_S8, 8,
  AI_PACK_INTQ_INFO(
    AI_PACK_INTQ_SCALE(0.005299325566738844f, 0.005511952098459005f, 0.003077686997130513f, 0.007012085523456335f, 0.005121184512972832f, 0.007750137709081173f, 0.005388062447309494f, 0.006717543583363295f),
    AI_PACK_INTQ_ZP(0, 0, 0, 0, 0, 0, 0, 0)))

/* Int quant #5 */
AI_INTQ_INFO_LIST_OBJ_DECLARE(tflpseudo_qconst4_intq, AI_STATIC_CONST,
  AI_BUFFER_META_FLAG_SCALE_FLOAT|AI_BUFFER_META_FLAG_ZEROPOINT_S8, 1,
  AI_PACK_INTQ_INFO(
    AI_PACK_INTQ_SCALE(0.0055044409818947315f),
    AI_PACK_INTQ_ZP(-64)))

/* Int quant #6 */
AI_INTQ_INFO_LIST_OBJ_DECLARE(conv2d_29_bias_intq, AI_STATIC_CONST,
  AI_BUFFER_META_FLAG_SCALE_FLOAT|AI_BUFFER_META_FLAG_ZEROPOINT_S8, 8,
  AI_PACK_INTQ_INFO(
    AI_PACK_INTQ_SCALE(0.00034662484540604055f, 0.0002679985191207379f, 0.0004089115827810019f, 0.0002040397230302915f, 0.00032826277310959995f, 0.000316268386086449f, 0.00023779337061569095f, 0.0002533410442993045f),
    AI_PACK_INTQ_ZP(0, 0, 0, 0, 0, 0, 0, 0)))

/* Int quant #7 */
AI_INTQ_INFO_LIST_OBJ_DECLARE(conv2d_29_weights_intq, AI_STATIC_CONST,
  AI_BUFFER_META_FLAG_SCALE_FLOAT|AI_BUFFER_META_FLAG_ZEROPOINT_S8, 8,
  AI_PACK_INTQ_INFO(
    AI_PACK_INTQ_SCALE(0.00539505435153842f, 0.004171272274106741f, 0.0063645183108747005f, 0.0031757832039147615f, 0.005109257064759731f, 0.0049225701950490475f, 0.0037011431995779276f, 0.003943135496228933f),
    AI_PACK_INTQ_ZP(0, 0, 0, 0, 0, 0, 0, 0)))

/* Int quant #8 */
AI_INTQ_INFO_LIST_OBJ_DECLARE(tflpseudo_qconst6_intq, AI_STATIC_CONST,
  AI_BUFFER_META_FLAG_SCALE_FLOAT|AI_BUFFER_META_FLAG_ZEROPOINT_S8, 1,
  AI_PACK_INTQ_INFO(
    AI_PACK_INTQ_SCALE(0.0014866824494674802f),
    AI_PACK_INTQ_ZP(-66)))

/* Int quant #9 */
AI_INTQ_INFO_LIST_OBJ_DECLARE(conv2d_23_bias_intq, AI_STATIC_CONST,
  AI_BUFFER_META_FLAG_SCALE_FLOAT|AI_BUFFER_META_FLAG_ZEROPOINT_S8, 8,
  AI_PACK_INTQ_INFO(
    AI_PACK_INTQ_SCALE(0.00042064295848831534f, 0.0003877074923366308f, 0.0009618368349038064f, 0.00042276064050383866f, 0.0005335368332453072f, 0.0003684471012093127f, 0.00026618383708409965f, 0.0005608134088106453f),
    AI_PACK_INTQ_ZP(0, 0, 0, 0, 0, 0, 0, 0)))

/* Int quant #10 */
AI_INTQ_INFO_LIST_OBJ_DECLARE(conv2d_23_weights_intq, AI_STATIC_CONST,
  AI_BUFFER_META_FLAG_SCALE_FLOAT|AI_BUFFER_META_FLAG_ZEROPOINT_S8, 8,
  AI_PACK_INTQ_INFO(
    AI_PACK_INTQ_SCALE(0.0035771110560745f, 0.0032970309257507324f, 0.00817937683314085f, 0.003595119807869196f, 0.004537150729447603f, 0.003133242018520832f, 0.002263604197651148f, 0.004769108723849058f),
    AI_PACK_INTQ_ZP(0, 0, 0, 0, 0, 0, 0, 0)))

/* Int quant #11 */
AI_INTQ_INFO_LIST_OBJ_DECLARE(tflpseudo_qconst8_intq, AI_STATIC_CONST,
  AI_BUFFER_META_FLAG_SCALE_FLOAT|AI_BUFFER_META_FLAG_ZEROPOINT_S8, 1,
  AI_PACK_INTQ_INFO(
    AI_PACK_INTQ_SCALE(0.0022567876148968935f),
    AI_PACK_INTQ_ZP(-18)))

/* Int quant #12 */
AI_INTQ_INFO_LIST_OBJ_DECLARE(tflpseudo_qconst9_intq, AI_STATIC_CONST,
  AI_BUFFER_META_FLAG_SCALE_FLOAT|AI_BUFFER_META_FLAG_ZEROPOINT_S8, 1,
  AI_PACK_INTQ_INFO(
    AI_PACK_INTQ_SCALE(0.002855363069102168f),
    AI_PACK_INTQ_ZP(-31)))

/* Int quant #13 */
AI_INTQ_INFO_LIST_OBJ_DECLARE(conv2d_10_bias_intq, AI_STATIC_CONST,
  AI_BUFFER_META_FLAG_SCALE_FLOAT|AI_BUFFER_META_FLAG_ZEROPOINT_S8, 8,
  AI_PACK_INTQ_INFO(
    AI_PACK_INTQ_SCALE(0.0003759492828976363f, 0.00024989896337501705f, 0.00012587927631102502f, 0.0002493732317816466f, 0.0002679963654372841f, 0.00022220102255232632f, 0.00018582245684228837f, 0.0003009349456988275f),
    AI_PACK_INTQ_ZP(0, 0, 0, 0, 0, 0, 0, 0)))

/* Int quant #14 */
AI_INTQ_INFO_LIST_OBJ_DECLARE(conv2d_10_weights_intq, AI_STATIC_CONST,
  AI_BUFFER_META_FLAG_SCALE_FLOAT|AI_BUFFER_META_FLAG_ZEROPOINT_S8, 8,
  AI_PACK_INTQ_INFO(
    AI_PACK_INTQ_SCALE(0.006029742304235697f, 0.004008057527244091f, 0.002018941333517432f, 0.0039996253326535225f, 0.004298316314816475f, 0.0035638180561363697f, 0.002980352845042944f, 0.004826608579605818f),
    AI_PACK_INTQ_ZP(0, 0, 0, 0, 0, 0, 0, 0)))

/* Int quant #15 */
AI_INTQ_INFO_LIST_OBJ_DECLARE(conv2d_9_bias_intq, AI_STATIC_CONST,
  AI_BUFFER_META_FLAG_SCALE_FLOAT|AI_BUFFER_META_FLAG_ZEROPOINT_S8, 8,
  AI_PACK_INTQ_INFO(
    AI_PACK_INTQ_SCALE(0.00026947353035211563f, 0.00019380307639949024f, 0.00010075099271489307f, 0.00030001814593560994f, 0.00026073845219798386f, 0.0003682218084577471f, 0.0001862060307757929f, 0.00028371743974275887f),
    AI_PACK_INTQ_ZP(0, 0, 0, 0, 0, 0, 0, 0)))

/* Int quant #16 */
AI_INTQ_INFO_LIST_OBJ_DECLARE(conv2d_9_weights_intq, AI_STATIC_CONST,
  AI_BUFFER_META_FLAG_SCALE_FLOAT|AI_BUFFER_META_FLAG_ZEROPOINT_S8, 8,
  AI_PACK_INTQ_INFO(
    AI_PACK_INTQ_SCALE(0.004322008229792118f, 0.0031083517242223024f, 0.001615916145965457f, 0.004811904393136501f, 0.004181908909231424f, 0.005905803292989731f, 0.0029865046963095665f, 0.004550462123006582f),
    AI_PACK_INTQ_ZP(0, 0, 0, 0, 0, 0, 0, 0)))

/* Int quant #17 */
AI_INTQ_INFO_LIST_OBJ_DECLARE(tflpseudo_qconst12_intq, AI_STATIC_CONST,
  AI_BUFFER_META_FLAG_SCALE_FLOAT|AI_BUFFER_META_FLAG_ZEROPOINT_S8, 1,
  AI_PACK_INTQ_INFO(
    AI_PACK_INTQ_SCALE(0.0036109494976699352f),
    AI_PACK_INTQ_ZP(-26)))

/* Int quant #18 */
AI_INTQ_INFO_LIST_OBJ_DECLARE(conv2d_3_bias_intq, AI_STATIC_CONST,
  AI_BUFFER_META_FLAG_SCALE_FLOAT|AI_BUFFER_META_FLAG_ZEROPOINT_S8, 8,
  AI_PACK_INTQ_INFO(
    AI_PACK_INTQ_SCALE(0.0006120079196989536f, 0.0005705238436348736f, 0.0006793113425374031f, 0.00048383025568909943f, 0.0005047076265327632f, 0.0006079343729652464f, 0.00043440033914521337f, 0.0004324620240367949f),
    AI_PACK_INTQ_ZP(0, 0, 0, 0, 0, 0, 0, 0)))

/* Int quant #19 */
AI_INTQ_INFO_LIST_OBJ_DECLARE(conv2d_3_weights_intq, AI_STATIC_CONST,
  AI_BUFFER_META_FLAG_SCALE_FLOAT|AI_BUFFER_META_FLAG_ZEROPOINT_S8, 8,
  AI_PACK_INTQ_INFO(
    AI_PACK_INTQ_SCALE(0.0051618097350001335f, 0.004811923950910568f, 0.005729461554437876f, 0.004080730956047773f, 0.004256815183907747f, 0.005127452313899994f, 0.003663828130811453f, 0.0036474799271672964f),
    AI_PACK_INTQ_ZP(0, 0, 0, 0, 0, 0, 0, 0)))

/* Int quant #20 */
AI_INTQ_INFO_LIST_OBJ_DECLARE(conversion_0_output_intq, AI_STATIC_CONST,
  AI_BUFFER_META_FLAG_SCALE_FLOAT|AI_BUFFER_META_FLAG_ZEROPOINT_S8, 1,
  AI_PACK_INTQ_INFO(
    AI_PACK_INTQ_SCALE(0.11856460571289062f),
    AI_PACK_INTQ_ZP(1)))

/* Int quant #21 */
AI_INTQ_INFO_LIST_OBJ_DECLARE(pad_1_output_intq, AI_STATIC_CONST,
  AI_BUFFER_META_FLAG_SCALE_FLOAT|AI_BUFFER_META_FLAG_ZEROPOINT_S8, 1,
  AI_PACK_INTQ_INFO(
    AI_PACK_INTQ_SCALE(0.11856460571289062f),
    AI_PACK_INTQ_ZP(1)))

/* Int quant #22 */
AI_INTQ_INFO_LIST_OBJ_DECLARE(conv2d_3_output_intq, AI_STATIC_CONST,
  AI_BUFFER_META_FLAG_SCALE_FLOAT|AI_BUFFER_META_FLAG_ZEROPOINT_S8, 1,
  AI_PACK_INTQ_INFO(
    AI_PACK_INTQ_SCALE(0.10719680786132812f),
    AI_PACK_INTQ_ZP(-20)))

/* Int quant #23 */
AI_INTQ_INFO_LIST_OBJ_DECLARE(eltwise_5_output_intq, AI_STATIC_CONST,
  AI_BUFFER_META_FLAG_SCALE_FLOAT|AI_BUFFER_META_FLAG_ZEROPOINT_S8, 1,
  AI_PACK_INTQ_INFO(
    AI_PACK_INTQ_SCALE(0.06234914809465408f),
    AI_PACK_INTQ_ZP(-128)))

/* Int quant #24 */
AI_INTQ_INFO_LIST_OBJ_DECLARE(conv2d_9_output_intq, AI_STATIC_CONST,
  AI_BUFFER_META_FLAG_SCALE_FLOAT|AI_BUFFER_META_FLAG_ZEROPOINT_S8, 1,
  AI_PACK_INTQ_INFO(
    AI_PACK_INTQ_SCALE(0.07453176379203796f),
    AI_PACK_INTQ_ZP(-11)))

/* Int quant #25 */
AI_INTQ_INFO_LIST_OBJ_DECLARE(eltwise_13_output_intq, AI_STATIC_CONST,
  AI_BUFFER_META_FLAG_SCALE_FLOAT|AI_BUFFER_META_FLAG_ZEROPOINT_S8, 1,
  AI_PACK_INTQ_INFO(
    AI_PACK_INTQ_SCALE(0.0747017189860344f),
    AI_PACK_INTQ_ZP(-8)))

/* Int quant #26 */
AI_INTQ_INFO_LIST_OBJ_DECLARE(pool_17_output_intq, AI_STATIC_CONST,
  AI_BUFFER_META_FLAG_SCALE_FLOAT|AI_BUFFER_META_FLAG_ZEROPOINT_S8, 1,
  AI_PACK_INTQ_INFO(
    AI_PACK_INTQ_SCALE(0.0747017189860344f),
    AI_PACK_INTQ_ZP(-8)))

/* Int quant #27 */
AI_INTQ_INFO_LIST_OBJ_DECLARE(pad_6_output_intq, AI_STATIC_CONST,
  AI_BUFFER_META_FLAG_SCALE_FLOAT|AI_BUFFER_META_FLAG_ZEROPOINT_S8, 1,
  AI_PACK_INTQ_INFO(
    AI_PACK_INTQ_SCALE(0.06234914809465408f),
    AI_PACK_INTQ_ZP(-128)))

/* Int quant #28 */
AI_INTQ_INFO_LIST_OBJ_DECLARE(conv2d_10_output_intq, AI_STATIC_CONST,
  AI_BUFFER_META_FLAG_SCALE_FLOAT|AI_BUFFER_META_FLAG_ZEROPOINT_S8, 1,
  AI_PACK_INTQ_INFO(
    AI_PACK_INTQ_SCALE(0.11648302525281906f),
    AI_PACK_INTQ_ZP(25)))

/* Int quant #29 */
AI_INTQ_INFO_LIST_OBJ_DECLARE(eltwise_14_output_intq, AI_STATIC_CONST,
  AI_BUFFER_META_FLAG_SCALE_FLOAT|AI_BUFFER_META_FLAG_ZEROPOINT_S8, 1,
  AI_PACK_INTQ_INFO(
    AI_PACK_INTQ_SCALE(0.11759292334318161f),
    AI_PACK_INTQ_ZP(25)))

/* Int quant #30 */
AI_INTQ_INFO_LIST_OBJ_DECLARE(pool_18_output_intq, AI_STATIC_CONST,
  AI_BUFFER_META_FLAG_SCALE_FLOAT|AI_BUFFER_META_FLAG_ZEROPOINT_S8, 1,
  AI_PACK_INTQ_INFO(
    AI_PACK_INTQ_SCALE(0.11759292334318161f),
    AI_PACK_INTQ_ZP(25)))

/* Int quant #31 */
AI_INTQ_INFO_LIST_OBJ_DECLARE(nl_18_output_intq, AI_STATIC_CONST,
  AI_BUFFER_META_FLAG_SCALE_FLOAT|AI_BUFFER_META_FLAG_ZEROPOINT_S8, 1,
  AI_PACK_INTQ_INFO(
    AI_PACK_INTQ_SCALE(0.11759292334318161f),
    AI_PACK_INTQ_ZP(25)))

/* Int quant #32 */
AI_INTQ_INFO_LIST_OBJ_DECLARE(pad_21_output_intq, AI_STATIC_CONST,
  AI_BUFFER_META_FLAG_SCALE_FLOAT|AI_BUFFER_META_FLAG_ZEROPOINT_S8, 1,
  AI_PACK_INTQ_INFO(
    AI_PACK_INTQ_SCALE(0.11759292334318161f),
    AI_PACK_INTQ_ZP(25)))

/* Int quant #33 */
AI_INTQ_INFO_LIST_OBJ_DECLARE(conv2d_23_output_intq, AI_STATIC_CONST,
  AI_BUFFER_META_FLAG_SCALE_FLOAT|AI_BUFFER_META_FLAG_ZEROPOINT_S8, 1,
  AI_PACK_INTQ_INFO(
    AI_PACK_INTQ_SCALE(0.10615453124046326f),
    AI_PACK_INTQ_ZP(23)))

/* Int quant #34 */
AI_INTQ_INFO_LIST_OBJ_DECLARE(eltwise_25_output_intq, AI_STATIC_CONST,
  AI_BUFFER_META_FLAG_SCALE_FLOAT|AI_BUFFER_META_FLAG_ZEROPOINT_S8, 1,
  AI_PACK_INTQ_INFO(
    AI_PACK_INTQ_SCALE(0.12678222358226776f),
    AI_PACK_INTQ_ZP(-2)))

/* Int quant #35 */
AI_INTQ_INFO_LIST_OBJ_DECLARE(eltwise_26_output_intq, AI_STATIC_CONST,
  AI_BUFFER_META_FLAG_SCALE_FLOAT|AI_BUFFER_META_FLAG_ZEROPOINT_S8, 1,
  AI_PACK_INTQ_INFO(
    AI_PACK_INTQ_SCALE(0.06424862891435623f),
    AI_PACK_INTQ_ZP(-128)))

/* Int quant #36 */
AI_INTQ_INFO_LIST_OBJ_DECLARE(pad_27_output_intq, AI_STATIC_CONST,
  AI_BUFFER_META_FLAG_SCALE_FLOAT|AI_BUFFER_META_FLAG_ZEROPOINT_S8, 1,
  AI_PACK_INTQ_INFO(
    AI_PACK_INTQ_SCALE(0.06424862891435623f),
    AI_PACK_INTQ_ZP(-128)))

/* Int quant #37 */
AI_INTQ_INFO_LIST_OBJ_DECLARE(conv2d_29_output_intq, AI_STATIC_CONST,
  AI_BUFFER_META_FLAG_SCALE_FLOAT|AI_BUFFER_META_FLAG_ZEROPOINT_S8, 1,
  AI_PACK_INTQ_INFO(
    AI_PACK_INTQ_SCALE(0.19851082563400269f),
    AI_PACK_INTQ_ZP(34)))

/* Int quant #38 */
AI_INTQ_INFO_LIST_OBJ_DECLARE(eltwise_31_output_intq, AI_STATIC_CONST,
  AI_BUFFER_META_FLAG_SCALE_FLOAT|AI_BUFFER_META_FLAG_ZEROPOINT_S8, 1,
  AI_PACK_INTQ_INFO(
    AI_PACK_INTQ_SCALE(0.07403960824012756f),
    AI_PACK_INTQ_ZP(-128)))

/* Int quant #39 */
AI_INTQ_INFO_LIST_OBJ_DECLARE(pad_32_output_intq, AI_STATIC_CONST,
  AI_BUFFER_META_FLAG_SCALE_FLOAT|AI_BUFFER_META_FLAG_ZEROPOINT_S8, 1,
  AI_PACK_INTQ_INFO(
    AI_PACK_INTQ_SCALE(0.07403960824012756f),
    AI_PACK_INTQ_ZP(-128)))

/* Int quant #40 */
AI_INTQ_INFO_LIST_OBJ_DECLARE(conv2d_34_output_intq, AI_STATIC_CONST,
  AI_BUFFER_META_FLAG_SCALE_FLOAT|AI_BUFFER_META_FLAG_ZEROPOINT_S8, 1,
  AI_PACK_INTQ_INFO(
    AI_PACK_INTQ_SCALE(0.16440701484680176f),
    AI_PACK_INTQ_ZP(37)))

/* Int quant #41 */
AI_INTQ_INFO_LIST_OBJ_DECLARE(eltwise_36_output_intq, AI_STATIC_CONST,
  AI_BUFFER_META_FLAG_SCALE_FLOAT|AI_BUFFER_META_FLAG_ZEROPOINT_S8, 1,
  AI_PACK_INTQ_INFO(
    AI_PACK_INTQ_SCALE(0.20797130465507507f),
    AI_PACK_INTQ_ZP(1)))

/* Int quant #42 */
AI_INTQ_INFO_LIST_OBJ_DECLARE(eltwise_37_output_intq, AI_STATIC_CONST,
  AI_BUFFER_META_FLAG_SCALE_FLOAT|AI_BUFFER_META_FLAG_ZEROPOINT_S8, 1,
  AI_PACK_INTQ_INFO(
    AI_PACK_INTQ_SCALE(0.10235848277807236f),
    AI_PACK_INTQ_ZP(-128)))

/* Int quant #43 */
AI_INTQ_INFO_LIST_OBJ_DECLARE(pool_39_output_intq, AI_STATIC_CONST,
  AI_BUFFER_META_FLAG_SCALE_FLOAT|AI_BUFFER_META_FLAG_ZEROPOINT_S8, 1,
  AI_PACK_INTQ_INFO(
    AI_PACK_INTQ_SCALE(0.10235848277807236f),
    AI_PACK_INTQ_ZP(-128)))

/* Int quant #44 */
AI_INTQ_INFO_LIST_OBJ_DECLARE(dense_40_output_intq, AI_STATIC_CONST,
  AI_BUFFER_META_FLAG_SCALE_FLOAT|AI_BUFFER_META_FLAG_ZEROPOINT_S8, 1,
  AI_PACK_INTQ_INFO(
    AI_PACK_INTQ_SCALE(0.07795906811952591f),
    AI_PACK_INTQ_ZP(-3)))

/**  Tensor declarations section  *********************************************/
/* Tensor #0 */
AI_TENSOR_OBJ_DECLARE(
  conv2d_34_scratch0, AI_STATIC,
  0x0, 0x0,
  AI_SHAPE_INIT(4, 1, 592, 1, 1), AI_STRIDE_INIT(4, 1, 1, 592, 592),
  1, &conv2d_34_scratch0_array, NULL)

/* Tensor #1 */
AI_TENSOR_OBJ_DECLARE(
  conv2d_29_scratch0, AI_STATIC,
  0x0, 0x0,
  AI_SHAPE_INIT(4, 1, 592, 1, 1), AI_STRIDE_INIT(4, 1, 1, 592, 592),
  1, &conv2d_29_scratch0_array, NULL)

/* Tensor #2 */
AI_TENSOR_OBJ_DECLARE(
  conv2d_23_scratch0, AI_STATIC,
  0x0, 0x0,
  AI_SHAPE_INIT(4, 1, 592, 1, 1), AI_STRIDE_INIT(4, 1, 1, 592, 592),
  1, &conv2d_23_scratch0_array, NULL)

/* Tensor #3 */
AI_TENSOR_OBJ_DECLARE(
  conv2d_10_scratch0, AI_STATIC,
  0x0, 0x0,
  AI_SHAPE_INIT(4, 1, 592, 1, 1), AI_STRIDE_INIT(4, 1, 1, 592, 592),
  1, &conv2d_10_scratch0_array, NULL)

/* Tensor #4 */
AI_TENSOR_OBJ_DECLARE(
  conv2d_9_scratch0, AI_STATIC,
  0x0, 0x0,
  AI_SHAPE_INIT(4, 1, 112, 1, 1), AI_STRIDE_INIT(4, 1, 1, 112, 112),
  1, &conv2d_9_scratch0_array, NULL)

/* Tensor #5 */
AI_TENSOR_OBJ_DECLARE(
  conv2d_3_scratch0, AI_STATIC,
  0x0, 0x0,
  AI_SHAPE_INIT(4, 1, 652, 1, 1), AI_STRIDE_INIT(4, 1, 1, 652, 652),
  1, &conv2d_3_scratch0_array, NULL)

/* Tensor #6 */
AI_TENSOR_OBJ_DECLARE(
  dense_40_bias, AI_STATIC,
  0x0, 0x0,
  AI_SHAPE_INIT(4, 1, 6, 1, 1), AI_STRIDE_INIT(4, 4, 4, 24, 24),
  1, &dense_40_bias_array, &dense_40_bias_intq)

/* Tensor #7 */
AI_TENSOR_OBJ_DECLARE(
  dense_40_weights, AI_STATIC,
  0x0, 0x0,
  AI_SHAPE_INIT(4, 8, 6, 1, 1), AI_STRIDE_INIT(4, 1, 8, 48, 48),
  1, &dense_40_weights_array, &dense_40_weights_intq)

/* Tensor #8 */
AI_TENSOR_OBJ_DECLARE(
  tflpseudo_qconst2, AI_STATIC,
  0x0, 0x0,
  AI_SHAPE_INIT(4, 1, 8, 1, 1), AI_STRIDE_INIT(4, 1, 1, 8, 8),
  1, &tflpseudo_qconst2_array, &tflpseudo_qconst2_intq)

/* Tensor #9 */
AI_TENSOR_OBJ_DECLARE(
  conv2d_34_bias, AI_STATIC,
  0x0, 0x0,
  AI_SHAPE_INIT(4, 1, 8, 1, 1), AI_STRIDE_INIT(4, 4, 4, 32, 32),
  1, &conv2d_34_bias_array, &conv2d_34_bias_intq)

/* Tensor #10 */
AI_TENSOR_OBJ_DECLARE(
  conv2d_34_weights, AI_STATIC,
  0x0, 0x0,
  AI_SHAPE_INIT(4, 8, 3, 1, 8), AI_STRIDE_INIT(4, 1, 8, 24, 24),
  1, &conv2d_34_weights_array, &conv2d_34_weights_intq)

/* Tensor #11 */
AI_TENSOR_OBJ_DECLARE(
  tflpseudo_qconst4, AI_STATIC,
  0x0, 0x0,
  AI_SHAPE_INIT(4, 1, 8, 1, 1), AI_STRIDE_INIT(4, 1, 1, 8, 8),
  1, &tflpseudo_qconst4_array, &tflpseudo_qconst4_intq)

/* Tensor #12 */
AI_TENSOR_OBJ_DECLARE(
  conv2d_29_bias, AI_STATIC,
  0x0, 0x0,
  AI_SHAPE_INIT(4, 1, 8, 1, 1), AI_STRIDE_INIT(4, 4, 4, 32, 32),
  1, &conv2d_29_bias_array, &conv2d_29_bias_intq)

/* Tensor #13 */
AI_TENSOR_OBJ_DECLARE(
  conv2d_29_weights, AI_STATIC,
  0x0, 0x0,
  AI_SHAPE_INIT(4, 8, 3, 1, 8), AI_STRIDE_INIT(4, 1, 8, 24, 24),
  1, &conv2d_29_weights_array, &conv2d_29_weights_intq)

/* Tensor #14 */
AI_TENSOR_OBJ_DECLARE(
  tflpseudo_qconst6, AI_STATIC,
  0x0, 0x0,
  AI_SHAPE_INIT(4, 1, 8, 1, 1), AI_STRIDE_INIT(4, 1, 1, 8, 8),
  1, &tflpseudo_qconst6_array, &tflpseudo_qconst6_intq)

/* Tensor #15 */
AI_TENSOR_OBJ_DECLARE(
  conv2d_23_bias, AI_STATIC,
  0x0, 0x0,
  AI_SHAPE_INIT(4, 1, 8, 1, 1), AI_STRIDE_INIT(4, 4, 4, 32, 32),
  1, &conv2d_23_bias_array, &conv2d_23_bias_intq)

/* Tensor #16 */
AI_TENSOR_OBJ_DECLARE(
  conv2d_23_weights, AI_STATIC,
  0x0, 0x0,
  AI_SHAPE_INIT(4, 8, 3, 1, 8), AI_STRIDE_INIT(4, 1, 8, 24, 24),
  1, &conv2d_23_weights_array, &conv2d_23_weights_intq)

/* Tensor #17 */
AI_TENSOR_OBJ_DECLARE(
  tflpseudo_qconst8, AI_STATIC,
  0x0, 0x0,
  AI_SHAPE_INIT(4, 1, 8, 1, 1), AI_STRIDE_INIT(4, 1, 1, 8, 8),
  1, &tflpseudo_qconst8_array, &tflpseudo_qconst8_intq)

/* Tensor #18 */
AI_TENSOR_OBJ_DECLARE(
  tflpseudo_qconst9, AI_STATIC,
  0x0, 0x0,
  AI_SHAPE_INIT(4, 1, 8, 1, 1), AI_STRIDE_INIT(4, 1, 1, 8, 8),
  1, &tflpseudo_qconst9_array, &tflpseudo_qconst9_intq)

/* Tensor #19 */
AI_TENSOR_OBJ_DECLARE(
  conv2d_10_bias, AI_STATIC,
  0x0, 0x0,
  AI_SHAPE_INIT(4, 1, 8, 1, 1), AI_STRIDE_INIT(4, 4, 4, 32, 32),
  1, &conv2d_10_bias_array, &conv2d_10_bias_intq)

/* Tensor #20 */
AI_TENSOR_OBJ_DECLARE(
  conv2d_10_weights, AI_STATIC,
  0x0, 0x0,
  AI_SHAPE_INIT(4, 8, 3, 1, 8), AI_STRIDE_INIT(4, 1, 8, 24, 24),
  1, &conv2d_10_weights_array, &conv2d_10_weights_intq)

/* Tensor #21 */
AI_TENSOR_OBJ_DECLARE(
  conv2d_9_bias, AI_STATIC,
  0x0, 0x0,
  AI_SHAPE_INIT(4, 1, 8, 1, 1), AI_STRIDE_INIT(4, 4, 4, 32, 32),
  1, &conv2d_9_bias_array, &conv2d_9_bias_intq)

/* Tensor #22 */
AI_TENSOR_OBJ_DECLARE(
  conv2d_9_weights, AI_STATIC,
  0x0, 0x0,
  AI_SHAPE_INIT(4, 8, 1, 1, 8), AI_STRIDE_INIT(4, 1, 8, 8, 8),
  1, &conv2d_9_weights_array, &conv2d_9_weights_intq)

/* Tensor #23 */
AI_TENSOR_OBJ_DECLARE(
  tflpseudo_qconst12, AI_STATIC,
  0x0, 0x0,
  AI_SHAPE_INIT(4, 1, 8, 1, 1), AI_STRIDE_INIT(4, 1, 1, 8, 8),
  1, &tflpseudo_qconst12_array, &tflpseudo_qconst12_intq)

/* Tensor #24 */
AI_TENSOR_OBJ_DECLARE(
  conv2d_3_bias, AI_STATIC,
  0x0, 0x0,
  AI_SHAPE_INIT(4, 1, 8, 1, 1), AI_STRIDE_INIT(4, 4, 4, 32, 32),
  1, &conv2d_3_bias_array, &conv2d_3_bias_intq)

/* Tensor #25 */
AI_TENSOR_OBJ_DECLARE(
  conv2d_3_weights, AI_STATIC,
  0x0, 0x0,
  AI_SHAPE_INIT(4, 9, 3, 1, 8), AI_STRIDE_INIT(4, 1, 9, 27, 27),
  1, &conv2d_3_weights_array, &conv2d_3_weights_intq)

/* Tensor #26 */
AI_TENSOR_OBJ_DECLARE(
  inputs_output, AI_STATIC,
  0x0, 0x0,
  AI_SHAPE_INIT(4, 1, 9, 128, 1), AI_STRIDE_INIT(4, 4, 4, 36, 4608),
  1, &inputs_output_array, NULL)

/* Tensor #27 */
AI_TENSOR_OBJ_DECLARE(
  conversion_0_output, AI_STATIC,
  0x0, 0x0,
  AI_SHAPE_INIT(4, 1, 9, 128, 1), AI_STRIDE_INIT(4, 1, 1, 9, 1152),
  1, &conversion_0_output_array, &conversion_0_output_intq)

/* Tensor #28 */
AI_TENSOR_OBJ_DECLARE(
  pad_1_output, AI_STATIC,
  0x0, 0x0,
  AI_SHAPE_INIT(4, 1, 9, 130, 1), AI_STRIDE_INIT(4, 1, 1, 9, 1170),
  1, &pad_1_output_array, &pad_1_output_intq)

/* Tensor #29 */
AI_TENSOR_OBJ_DECLARE(
  conv2d_3_output, AI_STATIC,
  0x0, 0x0,
  AI_SHAPE_INIT(4, 1, 8, 128, 1), AI_STRIDE_INIT(4, 1, 1, 8, 1024),
  1, &conv2d_3_output_array, &conv2d_3_output_intq)

/* Tensor #30 */
AI_TENSOR_OBJ_DECLARE(
  eltwise_5_output, AI_STATIC,
  0x0, 0x0,
  AI_SHAPE_INIT(4, 1, 8, 128, 1), AI_STRIDE_INIT(4, 1, 1, 8, 1024),
  1, &eltwise_5_output_array, &eltwise_5_output_intq)

/* Tensor #31 */
AI_TENSOR_OBJ_DECLARE(
  conv2d_9_output, AI_STATIC,
  0x0, 0x0,
  AI_SHAPE_INIT(4, 1, 8, 128, 1), AI_STRIDE_INIT(4, 1, 1, 8, 1024),
  1, &conv2d_9_output_array, &conv2d_9_output_intq)

/* Tensor #32 */
AI_TENSOR_OBJ_DECLARE(
  eltwise_13_output, AI_STATIC,
  0x0, 0x0,
  AI_SHAPE_INIT(4, 1, 8, 128, 1), AI_STRIDE_INIT(4, 1, 1, 8, 1024),
  1, &eltwise_13_output_array, &eltwise_13_output_intq)

/* Tensor #33 */
AI_TENSOR_OBJ_DECLARE(
  pool_17_output, AI_STATIC,
  0x0, 0x0,
  AI_SHAPE_INIT(4, 1, 8, 64, 1), AI_STRIDE_INIT(4, 1, 1, 8, 512),
  1, &pool_17_output_array, &pool_17_output_intq)

/* Tensor #34 */
AI_TENSOR_OBJ_DECLARE(
  pad_6_output, AI_STATIC,
  0x0, 0x0,
  AI_SHAPE_INIT(4, 1, 8, 130, 1), AI_STRIDE_INIT(4, 1, 1, 8, 1040),
  1, &pad_6_output_array, &pad_6_output_intq)

/* Tensor #35 */
AI_TENSOR_OBJ_DECLARE(
  conv2d_10_output, AI_STATIC,
  0x0, 0x0,
  AI_SHAPE_INIT(4, 1, 8, 128, 1), AI_STRIDE_INIT(4, 1, 1, 8, 1024),
  1, &conv2d_10_output_array, &conv2d_10_output_intq)

/* Tensor #36 */
AI_TENSOR_OBJ_DECLARE(
  eltwise_14_output, AI_STATIC,
  0x0, 0x0,
  AI_SHAPE_INIT(4, 1, 8, 128, 1), AI_STRIDE_INIT(4, 1, 1, 8, 1024),
  1, &eltwise_14_output_array, &eltwise_14_output_intq)

/* Tensor #37 */
AI_TENSOR_OBJ_DECLARE(
  pool_18_output, AI_STATIC,
  0x0, 0x0,
  AI_SHAPE_INIT(4, 1, 8, 64, 1), AI_STRIDE_INIT(4, 1, 1, 8, 512),
  1, &pool_18_output_array, &pool_18_output_intq)

/* Tensor #38 */
AI_TENSOR_OBJ_DECLARE(
  nl_18_output, AI_STATIC,
  0x0, 0x0,
  AI_SHAPE_INIT(4, 1, 8, 64, 1), AI_STRIDE_INIT(4, 1, 1, 8, 512),
  1, &nl_18_output_array, &nl_18_output_intq)

/* Tensor #39 */
AI_TENSOR_OBJ_DECLARE(
  pad_21_output, AI_STATIC,
  0x0, 0x0,
  AI_SHAPE_INIT(4, 1, 8, 66, 1), AI_STRIDE_INIT(4, 1, 1, 8, 528),
  1, &pad_21_output_array, &pad_21_output_intq)

/* Tensor #40 */
AI_TENSOR_OBJ_DECLARE(
  conv2d_23_output, AI_STATIC,
  0x0, 0x0,
  AI_SHAPE_INIT(4, 1, 8, 64, 1), AI_STRIDE_INIT(4, 1, 1, 8, 512),
  1, &conv2d_23_output_array, &conv2d_23_output_intq)

/* Tensor #41 */
AI_TENSOR_OBJ_DECLARE(
  eltwise_25_output, AI_STATIC,
  0x0, 0x0,
  AI_SHAPE_INIT(4, 1, 8, 64, 1), AI_STRIDE_INIT(4, 1, 1, 8, 512),
  1, &eltwise_25_output_array, &eltwise_25_output_intq)

/* Tensor #42 */
AI_TENSOR_OBJ_DECLARE(
  eltwise_26_output, AI_STATIC,
  0x0, 0x0,
  AI_SHAPE_INIT(4, 1, 8, 64, 1), AI_STRIDE_INIT(4, 1, 1, 8, 512),
  1, &eltwise_26_output_array, &eltwise_26_output_intq)

/* Tensor #43 */
AI_TENSOR_OBJ_DECLARE(
  pad_27_output, AI_STATIC,
  0x0, 0x0,
  AI_SHAPE_INIT(4, 1, 8, 66, 1), AI_STRIDE_INIT(4, 1, 1, 8, 528),
  1, &pad_27_output_array, &pad_27_output_intq)

/* Tensor #44 */
AI_TENSOR_OBJ_DECLARE(
  conv2d_29_output, AI_STATIC,
  0x0, 0x0,
  AI_SHAPE_INIT(4, 1, 8, 64, 1), AI_STRIDE_INIT(4, 1, 1, 8, 512),
  1, &conv2d_29_output_array, &conv2d_29_output_intq)

/* Tensor #45 */
AI_TENSOR_OBJ_DECLARE(
  eltwise_31_output, AI_STATIC,
  0x0, 0x0,
  AI_SHAPE_INIT(4, 1, 8, 64, 1), AI_STRIDE_INIT(4, 1, 1, 8, 512),
  1, &eltwise_31_output_array, &eltwise_31_output_intq)

/* Tensor #46 */
AI_TENSOR_OBJ_DECLARE(
  pad_32_output, AI_STATIC,
  0x0, 0x0,
  AI_SHAPE_INIT(4, 1, 8, 66, 1), AI_STRIDE_INIT(4, 1, 1, 8, 528),
  1, &pad_32_output_array, &pad_32_output_intq)

/* Tensor #47 */
AI_TENSOR_OBJ_DECLARE(
  conv2d_34_output, AI_STATIC,
  0x0, 0x0,
  AI_SHAPE_INIT(4, 1, 8, 64, 1), AI_STRIDE_INIT(4, 1, 1, 8, 512),
  1, &conv2d_34_output_array, &conv2d_34_output_intq)

/* Tensor #48 */
AI_TENSOR_OBJ_DECLARE(
  eltwise_36_output, AI_STATIC,
  0x0, 0x0,
  AI_SHAPE_INIT(4, 1, 8, 64, 1), AI_STRIDE_INIT(4, 1, 1, 8, 512),
  1, &eltwise_36_output_array, &eltwise_36_output_intq)

/* Tensor #49 */
AI_TENSOR_OBJ_DECLARE(
  eltwise_37_output, AI_STATIC,
  0x0, 0x0,
  AI_SHAPE_INIT(4, 1, 8, 64, 1), AI_STRIDE_INIT(4, 1, 1, 8, 512),
  1, &eltwise_37_output_array, &eltwise_37_output_intq)

/* Tensor #50 */
AI_TENSOR_OBJ_DECLARE(
  pool_39_output, AI_STATIC,
  0x0, 0x0,
  AI_SHAPE_INIT(4, 1, 8, 1, 1), AI_STRIDE_INIT(4, 1, 1, 8, 8),
  1, &pool_39_output_array, &pool_39_output_intq)

/* Tensor #51 */
AI_TENSOR_OBJ_DECLARE(
  dense_40_output, AI_STATIC,
  0x0, 0x0,
  AI_SHAPE_INIT(4, 1, 6, 1, 1), AI_STRIDE_INIT(4, 1, 1, 6, 6),
  1, &dense_40_output_array, &dense_40_output_intq)

/* Tensor #52 */
AI_TENSOR_OBJ_DECLARE(
  conversion_41_output, AI_STATIC,
  0x0, 0x0,
  AI_SHAPE_INIT(4, 1, 6, 1, 1), AI_STRIDE_INIT(4, 4, 4, 24, 24),
  1, &conversion_41_output_array, NULL)



/**  Layer declarations section  **********************************************/


AI_TENSOR_CHAIN_OBJ_DECLARE(
  conversion_0_chain, AI_STATIC_CONST, 4,
  AI_TENSOR_LIST_OBJ_INIT(AI_FLAG_NONE, 1, &inputs_output),
  AI_TENSOR_LIST_OBJ_INIT(AI_FLAG_NONE, 1, &conversion_0_output),
  AI_TENSOR_LIST_OBJ_EMPTY,
  AI_TENSOR_LIST_OBJ_EMPTY
)

AI_LAYER_OBJ_DECLARE(
  conversion_0_layer, 0,
  NL_TYPE,
  nl, node_convert,
  &AI_NET_OBJ_INSTANCE, &pad_1_layer, AI_STATIC,
  .tensors = &conversion_0_chain, 
)


AI_STATIC_CONST ai_i8 pad_1_value_data[] = { 1 };
AI_ARRAY_OBJ_DECLARE(
    pad_1_value, AI_ARRAY_FORMAT_S8,
    pad_1_value_data, pad_1_value_data, 1, AI_STATIC_CONST)
AI_TENSOR_CHAIN_OBJ_DECLARE(
  pad_1_chain, AI_STATIC_CONST, 4,
  AI_TENSOR_LIST_OBJ_INIT(AI_FLAG_NONE, 1, &conversion_0_output),
  AI_TENSOR_LIST_OBJ_INIT(AI_FLAG_NONE, 1, &pad_1_output),
  AI_TENSOR_LIST_OBJ_EMPTY,
  AI_TENSOR_LIST_OBJ_EMPTY
)

AI_LAYER_OBJ_DECLARE(
  pad_1_layer, 1,
  PAD_TYPE,
  pad, forward_pad,
  &AI_NET_OBJ_INSTANCE, &conv2d_3_layer, AI_STATIC,
  .tensors = &pad_1_chain, 
  .value = &pad_1_value, 
  .mode = AI_PAD_CONSTANT, 
  .pads = AI_SHAPE_INIT(4, 0, 1, 0, 1), 
)

AI_TENSOR_CHAIN_OBJ_DECLARE(
  conv2d_3_chain, AI_STATIC_CONST, 4,
  AI_TENSOR_LIST_OBJ_INIT(AI_FLAG_NONE, 1, &pad_1_output),
  AI_TENSOR_LIST_OBJ_INIT(AI_FLAG_NONE, 1, &conv2d_3_output),
  AI_TENSOR_LIST_OBJ_INIT(AI_FLAG_NONE, 3, &conv2d_3_weights, &conv2d_3_bias, NULL),
  AI_TENSOR_LIST_OBJ_INIT(AI_FLAG_NONE, 1, &conv2d_3_scratch0)
)

AI_LAYER_OBJ_DECLARE(
  conv2d_3_layer, 3,
  CONV2D_TYPE,
  conv2d, forward_conv2d_integer_SSSA_ch,
  &AI_NET_OBJ_INSTANCE, &eltwise_5_layer, AI_STATIC,
  .tensors = &conv2d_3_chain, 
  .groups = 1, 
  .nl_func = NULL, 
  .filter_stride = AI_SHAPE_2D_INIT(1, 1), 
  .dilation = AI_SHAPE_2D_INIT(1, 1), 
  .filter_pad = AI_SHAPE_INIT(4, 0, 0, 0, 0), 
)

AI_TENSOR_CHAIN_OBJ_DECLARE(
  eltwise_5_chain, AI_STATIC_CONST, 4,
  AI_TENSOR_LIST_OBJ_INIT(AI_FLAG_NONE, 2, &conv2d_3_output, &tflpseudo_qconst12),
  AI_TENSOR_LIST_OBJ_INIT(AI_FLAG_NONE, 1, &eltwise_5_output),
  AI_TENSOR_LIST_OBJ_EMPTY,
  AI_TENSOR_LIST_OBJ_EMPTY
)

AI_LAYER_OBJ_DECLARE(
  eltwise_5_layer, 5,
  ELTWISE_TYPE,
  eltwise, forward_add_integer_INT8,
  &AI_NET_OBJ_INSTANCE, &conv2d_9_layer, AI_STATIC,
  .tensors = &eltwise_5_chain, 
)

AI_TENSOR_CHAIN_OBJ_DECLARE(
  conv2d_9_chain, AI_STATIC_CONST, 4,
  AI_TENSOR_LIST_OBJ_INIT(AI_FLAG_NONE, 1, &eltwise_5_output),
  AI_TENSOR_LIST_OBJ_INIT(AI_FLAG_NONE, 1, &conv2d_9_output),
  AI_TENSOR_LIST_OBJ_INIT(AI_FLAG_NONE, 3, &conv2d_9_weights, &conv2d_9_bias, NULL),
  AI_TENSOR_LIST_OBJ_INIT(AI_FLAG_NONE, 1, &conv2d_9_scratch0)
)

AI_LAYER_OBJ_DECLARE(
  conv2d_9_layer, 9,
  CONV2D_TYPE,
  conv2d, forward_conv2d_integer_SSSA_ch,
  &AI_NET_OBJ_INSTANCE, &eltwise_13_layer, AI_STATIC,
  .tensors = &conv2d_9_chain, 
  .groups = 1, 
  .nl_func = NULL, 
  .filter_stride = AI_SHAPE_2D_INIT(1, 1), 
  .dilation = AI_SHAPE_2D_INIT(1, 1), 
  .filter_pad = AI_SHAPE_INIT(4, 0, 0, 0, 0), 
)

AI_TENSOR_CHAIN_OBJ_DECLARE(
  eltwise_13_chain, AI_STATIC_CONST, 4,
  AI_TENSOR_LIST_OBJ_INIT(AI_FLAG_NONE, 2, &conv2d_9_output, &tflpseudo_qconst9),
  AI_TENSOR_LIST_OBJ_INIT(AI_FLAG_NONE, 1, &eltwise_13_output),
  AI_TENSOR_LIST_OBJ_EMPTY,
  AI_TENSOR_LIST_OBJ_EMPTY
)

AI_LAYER_OBJ_DECLARE(
  eltwise_13_layer, 13,
  ELTWISE_TYPE,
  eltwise, forward_add_integer_INT8,
  &AI_NET_OBJ_INSTANCE, &pool_17_layer, AI_STATIC,
  .tensors = &eltwise_13_chain, 
)

AI_TENSOR_CHAIN_OBJ_DECLARE(
  pool_17_chain, AI_STATIC_CONST, 4,
  AI_TENSOR_LIST_OBJ_INIT(AI_FLAG_NONE, 1, &eltwise_13_output),
  AI_TENSOR_LIST_OBJ_INIT(AI_FLAG_NONE, 1, &pool_17_output),
  AI_TENSOR_LIST_OBJ_EMPTY,
  AI_TENSOR_LIST_OBJ_EMPTY
)

AI_LAYER_OBJ_DECLARE(
  pool_17_layer, 17,
  POOL_TYPE,
  pool, forward_mp_integer_INT8,
  &AI_NET_OBJ_INSTANCE, &pad_6_layer, AI_STATIC,
  .tensors = &pool_17_chain, 
  .pool_size = AI_SHAPE_2D_INIT(2, 1), 
  .pool_stride = AI_SHAPE_2D_INIT(2, 1), 
  .pool_pad = AI_SHAPE_INIT(4, 0, 0, 0, 0), 
)


AI_STATIC_CONST ai_i8 pad_6_value_data[] = { -128 };
AI_ARRAY_OBJ_DECLARE(
    pad_6_value, AI_ARRAY_FORMAT_S8,
    pad_6_value_data, pad_6_value_data, 1, AI_STATIC_CONST)
AI_TENSOR_CHAIN_OBJ_DECLARE(
  pad_6_chain, AI_STATIC_CONST, 4,
  AI_TENSOR_LIST_OBJ_INIT(AI_FLAG_NONE, 1, &eltwise_5_output),
  AI_TENSOR_LIST_OBJ_INIT(AI_FLAG_NONE, 1, &pad_6_output),
  AI_TENSOR_LIST_OBJ_EMPTY,
  AI_TENSOR_LIST_OBJ_EMPTY
)

AI_LAYER_OBJ_DECLARE(
  pad_6_layer, 6,
  PAD_TYPE,
  pad, forward_pad,
  &AI_NET_OBJ_INSTANCE, &conv2d_10_layer, AI_STATIC,
  .tensors = &pad_6_chain, 
  .value = &pad_6_value, 
  .mode = AI_PAD_CONSTANT, 
  .pads = AI_SHAPE_INIT(4, 0, 1, 0, 1), 
)

AI_TENSOR_CHAIN_OBJ_DECLARE(
  conv2d_10_chain, AI_STATIC_CONST, 4,
  AI_TENSOR_LIST_OBJ_INIT(AI_FLAG_NONE, 1, &pad_6_output),
  AI_TENSOR_LIST_OBJ_INIT(AI_FLAG_NONE, 1, &conv2d_10_output),
  AI_TENSOR_LIST_OBJ_INIT(AI_FLAG_NONE, 3, &conv2d_10_weights, &conv2d_10_bias, NULL),
  AI_TENSOR_LIST_OBJ_INIT(AI_FLAG_NONE, 1, &conv2d_10_scratch0)
)

AI_LAYER_OBJ_DECLARE(
  conv2d_10_layer, 10,
  CONV2D_TYPE,
  conv2d, forward_conv2d_integer_SSSA_ch,
  &AI_NET_OBJ_INSTANCE, &eltwise_14_layer, AI_STATIC,
  .tensors = &conv2d_10_chain, 
  .groups = 1, 
  .nl_func = NULL, 
  .filter_stride = AI_SHAPE_2D_INIT(1, 1), 
  .dilation = AI_SHAPE_2D_INIT(1, 1), 
  .filter_pad = AI_SHAPE_INIT(4, 0, 0, 0, 0), 
)

AI_TENSOR_CHAIN_OBJ_DECLARE(
  eltwise_14_chain, AI_STATIC_CONST, 4,
  AI_TENSOR_LIST_OBJ_INIT(AI_FLAG_NONE, 2, &conv2d_10_output, &tflpseudo_qconst8),
  AI_TENSOR_LIST_OBJ_INIT(AI_FLAG_NONE, 1, &eltwise_14_output),
  AI_TENSOR_LIST_OBJ_EMPTY,
  AI_TENSOR_LIST_OBJ_EMPTY
)

AI_LAYER_OBJ_DECLARE(
  eltwise_14_layer, 14,
  ELTWISE_TYPE,
  eltwise, forward_add_integer_INT8,
  &AI_NET_OBJ_INSTANCE, &pool_18_layer, AI_STATIC,
  .tensors = &eltwise_14_chain, 
)

AI_TENSOR_CHAIN_OBJ_DECLARE(
  pool_18_chain, AI_STATIC_CONST, 4,
  AI_TENSOR_LIST_OBJ_INIT(AI_FLAG_NONE, 1, &eltwise_14_output),
  AI_TENSOR_LIST_OBJ_INIT(AI_FLAG_NONE, 1, &pool_18_output),
  AI_TENSOR_LIST_OBJ_EMPTY,
  AI_TENSOR_LIST_OBJ_EMPTY
)

AI_LAYER_OBJ_DECLARE(
  pool_18_layer, 18,
  POOL_TYPE,
  pool, forward_mp_integer_INT8,
  &AI_NET_OBJ_INSTANCE, &nl_18_layer, AI_STATIC,
  .tensors = &pool_18_chain, 
  .pool_size = AI_SHAPE_2D_INIT(2, 1), 
  .pool_stride = AI_SHAPE_2D_INIT(2, 1), 
  .pool_pad = AI_SHAPE_INIT(4, 0, 0, 0, 0), 
)


AI_STATIC_CONST ai_i8 nl_18_nl_params_data[] = { 25 };
AI_ARRAY_OBJ_DECLARE(
    nl_18_nl_params, AI_ARRAY_FORMAT_S8,
    nl_18_nl_params_data, nl_18_nl_params_data, 1, AI_STATIC_CONST)
AI_TENSOR_CHAIN_OBJ_DECLARE(
  nl_18_chain, AI_STATIC_CONST, 4,
  AI_TENSOR_LIST_OBJ_INIT(AI_FLAG_NONE, 1, &pool_18_output),
  AI_TENSOR_LIST_OBJ_INIT(AI_FLAG_NONE, 1, &nl_18_output),
  AI_TENSOR_LIST_OBJ_EMPTY,
  AI_TENSOR_LIST_OBJ_EMPTY
)

AI_LAYER_OBJ_DECLARE(
  nl_18_layer, 18,
  NL_TYPE,
  nl, forward_relu_integer,
  &AI_NET_OBJ_INSTANCE, &pad_21_layer, AI_STATIC,
  .tensors = &nl_18_chain, 
  .nl_params = &nl_18_nl_params, 
)


AI_STATIC_CONST ai_i8 pad_21_value_data[] = { 25 };
AI_ARRAY_OBJ_DECLARE(
    pad_21_value, AI_ARRAY_FORMAT_S8,
    pad_21_value_data, pad_21_value_data, 1, AI_STATIC_CONST)
AI_TENSOR_CHAIN_OBJ_DECLARE(
  pad_21_chain, AI_STATIC_CONST, 4,
  AI_TENSOR_LIST_OBJ_INIT(AI_FLAG_NONE, 1, &nl_18_output),
  AI_TENSOR_LIST_OBJ_INIT(AI_FLAG_NONE, 1, &pad_21_output),
  AI_TENSOR_LIST_OBJ_EMPTY,
  AI_TENSOR_LIST_OBJ_EMPTY
)

AI_LAYER_OBJ_DECLARE(
  pad_21_layer, 21,
  PAD_TYPE,
  pad, forward_pad,
  &AI_NET_OBJ_INSTANCE, &conv2d_23_layer, AI_STATIC,
  .tensors = &pad_21_chain, 
  .value = &pad_21_value, 
  .mode = AI_PAD_CONSTANT, 
  .pads = AI_SHAPE_INIT(4, 0, 1, 0, 1), 
)

AI_TENSOR_CHAIN_OBJ_DECLARE(
  conv2d_23_chain, AI_STATIC_CONST, 4,
  AI_TENSOR_LIST_OBJ_INIT(AI_FLAG_NONE, 1, &pad_21_output),
  AI_TENSOR_LIST_OBJ_INIT(AI_FLAG_NONE, 1, &conv2d_23_output),
  AI_TENSOR_LIST_OBJ_INIT(AI_FLAG_NONE, 3, &conv2d_23_weights, &conv2d_23_bias, NULL),
  AI_TENSOR_LIST_OBJ_INIT(AI_FLAG_NONE, 1, &conv2d_23_scratch0)
)

AI_LAYER_OBJ_DECLARE(
  conv2d_23_layer, 23,
  CONV2D_TYPE,
  conv2d, forward_conv2d_integer_SSSA_ch,
  &AI_NET_OBJ_INSTANCE, &eltwise_25_layer, AI_STATIC,
  .tensors = &conv2d_23_chain, 
  .groups = 1, 
  .nl_func = NULL, 
  .filter_stride = AI_SHAPE_2D_INIT(1, 1), 
  .dilation = AI_SHAPE_2D_INIT(1, 1), 
  .filter_pad = AI_SHAPE_INIT(4, 0, 0, 0, 0), 
)

AI_TENSOR_CHAIN_OBJ_DECLARE(
  eltwise_25_chain, AI_STATIC_CONST, 4,
  AI_TENSOR_LIST_OBJ_INIT(AI_FLAG_NONE, 2, &conv2d_23_output, &tflpseudo_qconst6),
  AI_TENSOR_LIST_OBJ_INIT(AI_FLAG_NONE, 1, &eltwise_25_output),
  AI_TENSOR_LIST_OBJ_EMPTY,
  AI_TENSOR_LIST_OBJ_EMPTY
)

AI_LAYER_OBJ_DECLARE(
  eltwise_25_layer, 25,
  ELTWISE_TYPE,
  eltwise, forward_add_integer_INT8,
  &AI_NET_OBJ_INSTANCE, &eltwise_26_layer, AI_STATIC,
  .tensors = &eltwise_25_chain, 
)

AI_TENSOR_CHAIN_OBJ_DECLARE(
  eltwise_26_chain, AI_STATIC_CONST, 4,
  AI_TENSOR_LIST_OBJ_INIT(AI_FLAG_NONE, 2, &eltwise_25_output, &pool_17_output),
  AI_TENSOR_LIST_OBJ_INIT(AI_FLAG_NONE, 1, &eltwise_26_output),
  AI_TENSOR_LIST_OBJ_EMPTY,
  AI_TENSOR_LIST_OBJ_EMPTY
)

AI_LAYER_OBJ_DECLARE(
  eltwise_26_layer, 26,
  ELTWISE_TYPE,
  eltwise, forward_add_integer_INT8,
  &AI_NET_OBJ_INSTANCE, &pad_27_layer, AI_STATIC,
  .tensors = &eltwise_26_chain, 
)


AI_STATIC_CONST ai_i8 pad_27_value_data[] = { -128 };
AI_ARRAY_OBJ_DECLARE(
    pad_27_value, AI_ARRAY_FORMAT_S8,
    pad_27_value_data, pad_27_value_data, 1, AI_STATIC_CONST)
AI_TENSOR_CHAIN_OBJ_DECLARE(
  pad_27_chain, AI_STATIC_CONST, 4,
  AI_TENSOR_LIST_OBJ_INIT(AI_FLAG_NONE, 1, &eltwise_26_output),
  AI_TENSOR_LIST_OBJ_INIT(AI_FLAG_NONE, 1, &pad_27_output),
  AI_TENSOR_LIST_OBJ_EMPTY,
  AI_TENSOR_LIST_OBJ_EMPTY
)

AI_LAYER_OBJ_DECLARE(
  pad_27_layer, 27,
  PAD_TYPE,
  pad, forward_pad,
  &AI_NET_OBJ_INSTANCE, &conv2d_29_layer, AI_STATIC,
  .tensors = &pad_27_chain, 
  .value = &pad_27_value, 
  .mode = AI_PAD_CONSTANT, 
  .pads = AI_SHAPE_INIT(4, 0, 1, 0, 1), 
)

AI_TENSOR_CHAIN_OBJ_DECLARE(
  conv2d_29_chain, AI_STATIC_CONST, 4,
  AI_TENSOR_LIST_OBJ_INIT(AI_FLAG_NONE, 1, &pad_27_output),
  AI_TENSOR_LIST_OBJ_INIT(AI_FLAG_NONE, 1, &conv2d_29_output),
  AI_TENSOR_LIST_OBJ_INIT(AI_FLAG_NONE, 3, &conv2d_29_weights, &conv2d_29_bias, NULL),
  AI_TENSOR_LIST_OBJ_INIT(AI_FLAG_NONE, 1, &conv2d_29_scratch0)
)

AI_LAYER_OBJ_DECLARE(
  conv2d_29_layer, 29,
  CONV2D_TYPE,
  conv2d, forward_conv2d_integer_SSSA_ch,
  &AI_NET_OBJ_INSTANCE, &eltwise_31_layer, AI_STATIC,
  .tensors = &conv2d_29_chain, 
  .groups = 1, 
  .nl_func = NULL, 
  .filter_stride = AI_SHAPE_2D_INIT(1, 1), 
  .dilation = AI_SHAPE_2D_INIT(1, 1), 
  .filter_pad = AI_SHAPE_INIT(4, 0, 0, 0, 0), 
)

AI_TENSOR_CHAIN_OBJ_DECLARE(
  eltwise_31_chain, AI_STATIC_CONST, 4,
  AI_TENSOR_LIST_OBJ_INIT(AI_FLAG_NONE, 2, &conv2d_29_output, &tflpseudo_qconst4),
  AI_TENSOR_LIST_OBJ_INIT(AI_FLAG_NONE, 1, &eltwise_31_output),
  AI_TENSOR_LIST_OBJ_EMPTY,
  AI_TENSOR_LIST_OBJ_EMPTY
)

AI_LAYER_OBJ_DECLARE(
  eltwise_31_layer, 31,
  ELTWISE_TYPE,
  eltwise, forward_add_integer_INT8,
  &AI_NET_OBJ_INSTANCE, &pad_32_layer, AI_STATIC,
  .tensors = &eltwise_31_chain, 
)


AI_STATIC_CONST ai_i8 pad_32_value_data[] = { -128 };
AI_ARRAY_OBJ_DECLARE(
    pad_32_value, AI_ARRAY_FORMAT_S8,
    pad_32_value_data, pad_32_value_data, 1, AI_STATIC_CONST)
AI_TENSOR_CHAIN_OBJ_DECLARE(
  pad_32_chain, AI_STATIC_CONST, 4,
  AI_TENSOR_LIST_OBJ_INIT(AI_FLAG_NONE, 1, &eltwise_31_output),
  AI_TENSOR_LIST_OBJ_INIT(AI_FLAG_NONE, 1, &pad_32_output),
  AI_TENSOR_LIST_OBJ_EMPTY,
  AI_TENSOR_LIST_OBJ_EMPTY
)

AI_LAYER_OBJ_DECLARE(
  pad_32_layer, 32,
  PAD_TYPE,
  pad, forward_pad,
  &AI_NET_OBJ_INSTANCE, &conv2d_34_layer, AI_STATIC,
  .tensors = &pad_32_chain, 
  .value = &pad_32_value, 
  .mode = AI_PAD_CONSTANT, 
  .pads = AI_SHAPE_INIT(4, 0, 1, 0, 1), 
)

AI_TENSOR_CHAIN_OBJ_DECLARE(
  conv2d_34_chain, AI_STATIC_CONST, 4,
  AI_TENSOR_LIST_OBJ_INIT(AI_FLAG_NONE, 1, &pad_32_output),
  AI_TENSOR_LIST_OBJ_INIT(AI_FLAG_NONE, 1, &conv2d_34_output),
  AI_TENSOR_LIST_OBJ_INIT(AI_FLAG_NONE, 3, &conv2d_34_weights, &conv2d_34_bias, NULL),
  AI_TENSOR_LIST_OBJ_INIT(AI_FLAG_NONE, 1, &conv2d_34_scratch0)
)

AI_LAYER_OBJ_DECLARE(
  conv2d_34_layer, 34,
  CONV2D_TYPE,
  conv2d, forward_conv2d_integer_SSSA_ch,
  &AI_NET_OBJ_INSTANCE, &eltwise_36_layer, AI_STATIC,
  .tensors = &conv2d_34_chain, 
  .groups = 1, 
  .nl_func = NULL, 
  .filter_stride = AI_SHAPE_2D_INIT(1, 1), 
  .dilation = AI_SHAPE_2D_INIT(1, 1), 
  .filter_pad = AI_SHAPE_INIT(4, 0, 0, 0, 0), 
)

AI_TENSOR_CHAIN_OBJ_DECLARE(
  eltwise_36_chain, AI_STATIC_CONST, 4,
  AI_TENSOR_LIST_OBJ_INIT(AI_FLAG_NONE, 2, &conv2d_34_output, &tflpseudo_qconst2),
  AI_TENSOR_LIST_OBJ_INIT(AI_FLAG_NONE, 1, &eltwise_36_output),
  AI_TENSOR_LIST_OBJ_EMPTY,
  AI_TENSOR_LIST_OBJ_EMPTY
)

AI_LAYER_OBJ_DECLARE(
  eltwise_36_layer, 36,
  ELTWISE_TYPE,
  eltwise, forward_add_integer_INT8,
  &AI_NET_OBJ_INSTANCE, &eltwise_37_layer, AI_STATIC,
  .tensors = &eltwise_36_chain, 
)

AI_TENSOR_CHAIN_OBJ_DECLARE(
  eltwise_37_chain, AI_STATIC_CONST, 4,
  AI_TENSOR_LIST_OBJ_INIT(AI_FLAG_NONE, 2, &eltwise_36_output, &eltwise_26_output),
  AI_TENSOR_LIST_OBJ_INIT(AI_FLAG_NONE, 1, &eltwise_37_output),
  AI_TENSOR_LIST_OBJ_EMPTY,
  AI_TENSOR_LIST_OBJ_EMPTY
)

AI_LAYER_OBJ_DECLARE(
  eltwise_37_layer, 37,
  ELTWISE_TYPE,
  eltwise, forward_add_integer_INT8,
  &AI_NET_OBJ_INSTANCE, &pool_39_layer, AI_STATIC,
  .tensors = &eltwise_37_chain, 
)

AI_TENSOR_CHAIN_OBJ_DECLARE(
  pool_39_chain, AI_STATIC_CONST, 4,
  AI_TENSOR_LIST_OBJ_INIT(AI_FLAG_NONE, 1, &eltwise_37_output),
  AI_TENSOR_LIST_OBJ_INIT(AI_FLAG_NONE, 1, &pool_39_output),
  AI_TENSOR_LIST_OBJ_EMPTY,
  AI_TENSOR_LIST_OBJ_EMPTY
)

AI_LAYER_OBJ_DECLARE(
  pool_39_layer, 39,
  POOL_TYPE,
  pool, forward_mp_integer_INT8,
  &AI_NET_OBJ_INSTANCE, &dense_40_layer, AI_STATIC,
  .tensors = &pool_39_chain, 
  .pool_size = AI_SHAPE_2D_INIT(64, 1), 
  .pool_stride = AI_SHAPE_2D_INIT(64, 1), 
  .pool_pad = AI_SHAPE_INIT(4, 0, 0, 0, 0), 
)

AI_TENSOR_CHAIN_OBJ_DECLARE(
  dense_40_chain, AI_STATIC_CONST, 4,
  AI_TENSOR_LIST_OBJ_INIT(AI_FLAG_NONE, 1, &pool_39_output),
  AI_TENSOR_LIST_OBJ_INIT(AI_FLAG_NONE, 1, &dense_40_output),
  AI_TENSOR_LIST_OBJ_INIT(AI_FLAG_NONE, 2, &dense_40_weights, &dense_40_bias),
  AI_TENSOR_LIST_OBJ_EMPTY
)

AI_LAYER_OBJ_DECLARE(
  dense_40_layer, 40,
  DENSE_TYPE,
  dense, forward_dense_integer_SSSA,
  &AI_NET_OBJ_INSTANCE, &conversion_41_layer, AI_STATIC,
  .tensors = &dense_40_chain, 
)

AI_TENSOR_CHAIN_OBJ_DECLARE(
  conversion_41_chain, AI_STATIC_CONST, 4,
  AI_TENSOR_LIST_OBJ_INIT(AI_FLAG_NONE, 1, &dense_40_output),
  AI_TENSOR_LIST_OBJ_INIT(AI_FLAG_NONE, 1, &conversion_41_output),
  AI_TENSOR_LIST_OBJ_EMPTY,
  AI_TENSOR_LIST_OBJ_EMPTY
)

AI_LAYER_OBJ_DECLARE(
  conversion_41_layer, 41,
  NL_TYPE,
  nl, node_convert,
  &AI_NET_OBJ_INSTANCE, &conversion_41_layer, AI_STATIC,
  .tensors = &conversion_41_chain, 
)


AI_NETWORK_OBJ_DECLARE(
  AI_NET_OBJ_INSTANCE, AI_STATIC,
  AI_BUFFER_OBJ_INIT(AI_BUFFER_FORMAT_U8,
                     1, 1, 1360, 1,
                     NULL),
  AI_BUFFER_OBJ_INIT(AI_BUFFER_FORMAT_U8,
                     1, 1, 3168, 1,
                     NULL),
  AI_TENSOR_LIST_IO_OBJ_INIT(AI_FLAG_NONE, AI_NETWORK_IN_NUM, &inputs_output),
  AI_TENSOR_LIST_IO_OBJ_INIT(AI_FLAG_NONE, AI_NETWORK_OUT_NUM, &conversion_41_output),
  &conversion_0_layer, 0, NULL)



AI_DECLARE_STATIC
ai_bool network_configure_activations(
  ai_network* net_ctx, const ai_buffer* activation_buffer)
{
  AI_ASSERT(net_ctx &&  activation_buffer && activation_buffer->data)

  ai_ptr activations = AI_PTR(AI_PTR_ALIGN(activation_buffer->data, AI_NETWORK_ACTIVATIONS_ALIGNMENT));
  AI_ASSERT(activations)
  AI_UNUSED(net_ctx)

  {
    /* Updating activations (byte) offsets */
    conv2d_34_scratch0_array.data = AI_PTR(activations + 2064);
    conv2d_34_scratch0_array.data_start = AI_PTR(activations + 2064);
    conv2d_29_scratch0_array.data = AI_PTR(activations + 1552);
    conv2d_29_scratch0_array.data_start = AI_PTR(activations + 1552);
    conv2d_23_scratch0_array.data = AI_PTR(activations + 0);
    conv2d_23_scratch0_array.data_start = AI_PTR(activations + 0);
    conv2d_10_scratch0_array.data = AI_PTR(activations + 1024);
    conv2d_10_scratch0_array.data_start = AI_PTR(activations + 1024);
    conv2d_9_scratch0_array.data = AI_PTR(activations + 2944);
    conv2d_9_scratch0_array.data_start = AI_PTR(activations + 2944);
    conv2d_3_scratch0_array.data = AI_PTR(activations + 80);
    conv2d_3_scratch0_array.data_start = AI_PTR(activations + 80);
    inputs_output_array.data = AI_PTR(NULL);
    inputs_output_array.data_start = AI_PTR(NULL);
    conversion_0_output_array.data = AI_PTR(activations + 1904);
    conversion_0_output_array.data_start = AI_PTR(activations + 1904);
    pad_1_output_array.data = AI_PTR(activations + 732);
    pad_1_output_array.data_start = AI_PTR(activations + 732);
    conv2d_3_output_array.data = AI_PTR(activations + 2032);
    conv2d_3_output_array.data_start = AI_PTR(activations + 2032);
    eltwise_5_output_array.data = AI_PTR(activations + 80);
    eltwise_5_output_array.data_start = AI_PTR(activations + 80);
    conv2d_9_output_array.data = AI_PTR(activations + 1104);
    conv2d_9_output_array.data_start = AI_PTR(activations + 1104);
    eltwise_13_output_array.data = AI_PTR(activations + 2128);
    eltwise_13_output_array.data_start = AI_PTR(activations + 2128);
    pool_17_output_array.data = AI_PTR(activations + 1616);
    pool_17_output_array.data_start = AI_PTR(activations + 1616);
    pad_6_output_array.data = AI_PTR(activations + 2128);
    pad_6_output_array.data_start = AI_PTR(activations + 2128);
    conv2d_10_output_array.data = AI_PTR(activations + 0);
    conv2d_10_output_array.data_start = AI_PTR(activations + 0);
    eltwise_14_output_array.data = AI_PTR(activations + 2128);
    eltwise_14_output_array.data_start = AI_PTR(activations + 2128);
    pool_18_output_array.data = AI_PTR(activations + 0);
    pool_18_output_array.data_start = AI_PTR(activations + 0);
    nl_18_output_array.data = AI_PTR(activations + 512);
    nl_18_output_array.data_start = AI_PTR(activations + 512);
    pad_21_output_array.data = AI_PTR(activations + 1024);
    pad_21_output_array.data_start = AI_PTR(activations + 1024);
    conv2d_23_output_array.data = AI_PTR(activations + 2128);
    conv2d_23_output_array.data_start = AI_PTR(activations + 2128);
    eltwise_25_output_array.data = AI_PTR(activations + 0);
    eltwise_25_output_array.data_start = AI_PTR(activations + 0);
    eltwise_26_output_array.data = AI_PTR(activations + 512);
    eltwise_26_output_array.data_start = AI_PTR(activations + 512);
    pad_27_output_array.data = AI_PTR(activations + 1024);
    pad_27_output_array.data_start = AI_PTR(activations + 1024);
    conv2d_29_output_array.data = AI_PTR(activations + 0);
    conv2d_29_output_array.data_start = AI_PTR(activations + 0);
    eltwise_31_output_array.data = AI_PTR(activations + 1024);
    eltwise_31_output_array.data_start = AI_PTR(activations + 1024);
    pad_32_output_array.data = AI_PTR(activations + 1536);
    pad_32_output_array.data_start = AI_PTR(activations + 1536);
    conv2d_34_output_array.data = AI_PTR(activations + 0);
    conv2d_34_output_array.data_start = AI_PTR(activations + 0);
    eltwise_36_output_array.data = AI_PTR(activations + 1024);
    eltwise_36_output_array.data_start = AI_PTR(activations + 1024);
    eltwise_37_output_array.data = AI_PTR(activations + 0);
    eltwise_37_output_array.data_start = AI_PTR(activations + 0);
    pool_39_output_array.data = AI_PTR(activations + 512);
    pool_39_output_array.data_start = AI_PTR(activations + 512);
    dense_40_output_array.data = AI_PTR(activations + 0);
    dense_40_output_array.data_start = AI_PTR(activations + 0);
    conversion_41_output_array.data = AI_PTR(NULL);
    conversion_41_output_array.data_start = AI_PTR(NULL);
    
  }
  return true;
}



AI_DECLARE_STATIC
ai_bool network_configure_weights(
  ai_network* net_ctx, const ai_buffer* weights_buffer)
{
  AI_ASSERT(net_ctx &&  weights_buffer && weights_buffer->data)

  ai_ptr weights = AI_PTR(weights_buffer->data);
  AI_ASSERT(weights)
  AI_UNUSED(net_ctx)

  {
    /* Updating weights (byte) offsets */
    
    dense_40_bias_array.format |= AI_FMT_FLAG_CONST;
    dense_40_bias_array.data = AI_PTR(weights + 1336);
    dense_40_bias_array.data_start = AI_PTR(weights + 1336);
    dense_40_weights_array.format |= AI_FMT_FLAG_CONST;
    dense_40_weights_array.data = AI_PTR(weights + 1288);
    dense_40_weights_array.data_start = AI_PTR(weights + 1288);
    tflpseudo_qconst2_array.format |= AI_FMT_FLAG_CONST;
    tflpseudo_qconst2_array.data = AI_PTR(weights + 1280);
    tflpseudo_qconst2_array.data_start = AI_PTR(weights + 1280);
    conv2d_34_bias_array.format |= AI_FMT_FLAG_CONST;
    conv2d_34_bias_array.data = AI_PTR(weights + 1248);
    conv2d_34_bias_array.data_start = AI_PTR(weights + 1248);
    conv2d_34_weights_array.format |= AI_FMT_FLAG_CONST;
    conv2d_34_weights_array.data = AI_PTR(weights + 1056);
    conv2d_34_weights_array.data_start = AI_PTR(weights + 1056);
    tflpseudo_qconst4_array.format |= AI_FMT_FLAG_CONST;
    tflpseudo_qconst4_array.data = AI_PTR(weights + 1048);
    tflpseudo_qconst4_array.data_start = AI_PTR(weights + 1048);
    conv2d_29_bias_array.format |= AI_FMT_FLAG_CONST;
    conv2d_29_bias_array.data = AI_PTR(weights + 1016);
    conv2d_29_bias_array.data_start = AI_PTR(weights + 1016);
    conv2d_29_weights_array.format |= AI_FMT_FLAG_CONST;
    conv2d_29_weights_array.data = AI_PTR(weights + 824);
    conv2d_29_weights_array.data_start = AI_PTR(weights + 824);
    tflpseudo_qconst6_array.format |= AI_FMT_FLAG_CONST;
    tflpseudo_qconst6_array.data = AI_PTR(weights + 816);
    tflpseudo_qconst6_array.data_start = AI_PTR(weights + 816);
    conv2d_23_bias_array.format |= AI_FMT_FLAG_CONST;
    conv2d_23_bias_array.data = AI_PTR(weights + 784);
    conv2d_23_bias_array.data_start = AI_PTR(weights + 784);
    conv2d_23_weights_array.format |= AI_FMT_FLAG_CONST;
    conv2d_23_weights_array.data = AI_PTR(weights + 592);
    conv2d_23_weights_array.data_start = AI_PTR(weights + 592);
    tflpseudo_qconst8_array.format |= AI_FMT_FLAG_CONST;
    tflpseudo_qconst8_array.data = AI_PTR(weights + 584);
    tflpseudo_qconst8_array.data_start = AI_PTR(weights + 584);
    tflpseudo_qconst9_array.format |= AI_FMT_FLAG_CONST;
    tflpseudo_qconst9_array.data = AI_PTR(weights + 576);
    tflpseudo_qconst9_array.data_start = AI_PTR(weights + 576);
    conv2d_10_bias_array.format |= AI_FMT_FLAG_CONST;
    conv2d_10_bias_array.data = AI_PTR(weights + 544);
    conv2d_10_bias_array.data_start = AI_PTR(weights + 544);
    conv2d_10_weights_array.format |= AI_FMT_FLAG_CONST;
    conv2d_10_weights_array.data = AI_PTR(weights + 352);
    conv2d_10_weights_array.data_start = AI_PTR(weights + 352);
    conv2d_9_bias_array.format |= AI_FMT_FLAG_CONST;
    conv2d_9_bias_array.data = AI_PTR(weights + 320);
    conv2d_9_bias_array.data_start = AI_PTR(weights + 320);
    conv2d_9_weights_array.format |= AI_FMT_FLAG_CONST;
    conv2d_9_weights_array.data = AI_PTR(weights + 256);
    conv2d_9_weights_array.data_start = AI_PTR(weights + 256);
    tflpseudo_qconst12_array.format |= AI_FMT_FLAG_CONST;
    tflpseudo_qconst12_array.data = AI_PTR(weights + 248);
    tflpseudo_qconst12_array.data_start = AI_PTR(weights + 248);
    conv2d_3_bias_array.format |= AI_FMT_FLAG_CONST;
    conv2d_3_bias_array.data = AI_PTR(weights + 216);
    conv2d_3_bias_array.data_start = AI_PTR(weights + 216);
    conv2d_3_weights_array.format |= AI_FMT_FLAG_CONST;
    conv2d_3_weights_array.data = AI_PTR(weights + 0);
    conv2d_3_weights_array.data_start = AI_PTR(weights + 0);
  }

  return true;
}


/**  PUBLIC APIs SECTION  *****************************************************/

AI_API_ENTRY
ai_bool ai_network_get_info(
  ai_handle network, ai_network_report* report)
{
  ai_network* net_ctx = AI_NETWORK_ACQUIRE_CTX(network);

  if ( report && net_ctx )
  {
    ai_network_report r = {
      .model_name        = AI_NETWORK_MODEL_NAME,
      .model_signature   = AI_NETWORK_MODEL_SIGNATURE,
      .model_datetime    = AI_TOOLS_DATE_TIME,
      
      .compile_datetime  = AI_TOOLS_COMPILE_TIME,
      
      .runtime_revision  = ai_platform_runtime_get_revision(),
      .runtime_version   = ai_platform_runtime_get_version(),

      .tool_revision     = AI_TOOLS_REVISION_ID,
      .tool_version      = {AI_TOOLS_VERSION_MAJOR, AI_TOOLS_VERSION_MINOR,
                            AI_TOOLS_VERSION_MICRO, 0x0},
      .tool_api_version  = {AI_TOOLS_API_VERSION_MAJOR, AI_TOOLS_API_VERSION_MINOR,
                            AI_TOOLS_API_VERSION_MICRO, 0x0},

      .api_version            = ai_platform_api_get_version(),
      .interface_api_version  = ai_platform_interface_api_get_version(),
      
      .n_macc            = 108396,
      .n_inputs          = 0,
      .inputs            = NULL,
      .n_outputs         = 0,
      .outputs           = NULL,
      .activations       = AI_STRUCT_INIT,
      .params            = AI_STRUCT_INIT,
      .n_nodes           = 0,
      .signature         = 0x0,
    };

    if ( !ai_platform_api_get_network_report(network, &r) ) return false;

    *report = r;
    return true;
  }

  return false;
}

AI_API_ENTRY
ai_error ai_network_get_error(ai_handle network)
{
  return ai_platform_network_get_error(network);
}

AI_API_ENTRY
ai_error ai_network_create(
  ai_handle* network, const ai_buffer* network_config)
{
  return ai_platform_network_create(
    network, network_config, 
    &AI_NET_OBJ_INSTANCE,
    AI_TOOLS_API_VERSION_MAJOR, AI_TOOLS_API_VERSION_MINOR, AI_TOOLS_API_VERSION_MICRO);
}

AI_API_ENTRY
ai_handle ai_network_destroy(ai_handle network)
{
  return ai_platform_network_destroy(network);
}

AI_API_ENTRY
ai_bool ai_network_init(
  ai_handle network, const ai_network_params* params)
{
  ai_network* net_ctx = ai_platform_network_init(network, params);
  if ( !net_ctx ) return false;

  ai_bool ok = true;
  ok &= network_configure_weights(net_ctx, &params->params);
  ok &= network_configure_activations(net_ctx, &params->activations);

  ok &= ai_platform_network_post_init(network);

  return ok;
}


AI_API_ENTRY
ai_i32 ai_network_run(
  ai_handle network, const ai_buffer* input, ai_buffer* output)
{
  return ai_platform_network_process(network, input, output);
}

AI_API_ENTRY
ai_i32 ai_network_forward(ai_handle network, const ai_buffer* input)
{
  return ai_platform_network_process(network, input, NULL);
}




#undef AI_NETWORK_MODEL_SIGNATURE
#undef AI_NET_OBJ_INSTANCE
#undef AI_TOOLS_VERSION_MAJOR
#undef AI_TOOLS_VERSION_MINOR
#undef AI_TOOLS_VERSION_MICRO
#undef AI_TOOLS_API_VERSION_MAJOR
#undef AI_TOOLS_API_VERSION_MINOR
#undef AI_TOOLS_API_VERSION_MICRO
#undef AI_TOOLS_DATE_TIME
#undef AI_TOOLS_COMPILE_TIME

