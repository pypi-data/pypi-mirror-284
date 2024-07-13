**********************
L4S FrameBlasting Flow
**********************

.. code-block:: json

   {
      "type":  "l4s_frame_blasting",
      "name":  "<flow_name:str>",
      "source": {
            "port_group": [
               "<source_group:str>"
            ]
      },
      "destination": {
            "port_group": [
               "<destination_group:str>"
            ]
      },
      "l4s_ecn": "<l4s_ecn_marking_type:str>",
      "dscp": "<dscp_code_point:str|int>",
      "add_reverse_direction": "<add_reverse_direction_flow:bool>",
      "initial_time_to_wait": "<initial_time_to_wait:float|int|timedelta>",
      "bitrate": "<flow_bitrate:float>",
      "frame_size": "<frame_size_without_crc:int>",
      "frame_rate": "<frame_rate:float>",
      "number_of_frames": "<number_of_frames:float>",
      "duration": "<flow_duration:float|int|timedelta>",
      "udp_src": "<udp_source_port:int>",
      "udp_dest": "<udp_destination_port:int>",
      "nat_keep_alive": "<activate_nat_keep_alive:bool>",
      "analysis": {
         "latency":"<enable_latency_analysis:bool>",
         "max_threshold_latency": "<max_threshold_latency:float>",
         "max_loss_percentage": "<max_loss_percentage:float>",
         "quantile": "<quantile:float>",
         "min_percentile": "<min_percentile:float>",
         "max_percentile": "<max_percentile:float>"
      }
   }


.. jsonschema:: ../extra/test-cases/low-latency/json/config-schema.json#/$defs/l4s_frame_blasting_flow
   :auto_reference:
   :auto_target:
   :lift_title: False
