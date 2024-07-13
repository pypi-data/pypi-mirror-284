use wasm_bindgen::prelude::*;
use transportations_library::{ TwoLaneHighways, Segment, SubSegment };

#[wasm_bindgen]
#[derive(Debug, Clone)]
pub struct WasmSubSegment {
    inner: SubSegment,
}

#[wasm_bindgen]
impl WasmSubSegment {

    #[wasm_bindgen(constructor)]
    pub fn new(length: f64, avg_speed: f64, hor_class: i32, design_rad: f64, central_angle: f64, sup_ele: f64) -> Self {
        WasmSubSegment {

            inner: SubSegment::new(
                length,
                avg_speed,
                hor_class,
                design_rad,
                central_angle,
                sup_ele,
            ),
        }
    }

    pub fn to_js_value(&self) -> JsValue {
        let obj = js_sys::Object::new();
        js_sys::Reflect::set(&obj, &JsValue::from_str("length"), &JsValue::from(self.get_length())).unwrap();
        js_sys::Reflect::set(&obj, &JsValue::from_str("avg_speed"), &JsValue::from(self.get_avg_speed())).unwrap();
        js_sys::Reflect::set(&obj, &JsValue::from_str("hor_class"), &JsValue::from(self.get_hor_class())).unwrap();
        js_sys::Reflect::set(&obj, &JsValue::from_str("design_rad"), &JsValue::from(self.get_design_rad())).unwrap();
        js_sys::Reflect::set(&obj, &JsValue::from_str("central_angle"), &JsValue::from(self.get_central_angle())).unwrap();
        js_sys::Reflect::set(&obj, &JsValue::from_str("sup_ele"), &JsValue::from(self.get_sup_ele())).unwrap();
        
        // Convert the JavaScript object to a JsValue
        JsValue::from(obj)
    }

    pub fn get_length(&self) -> f64 {
        self.inner.get_length()
    }

    pub fn get_avg_speed(&self) -> f64 {
        self.inner.get_avg_speed()
    }

    pub fn get_hor_class(&self) -> i32 {
        self.inner.get_hor_class()
    }

    pub fn get_design_rad(&self) -> f64 {
        self.inner.get_design_rad()
    }
    
    pub fn get_central_angle(&self) -> f64 {
        self.inner.get_central_angle()
    }

    pub fn get_sup_ele(&self) -> f64 {
        self.inner.get_sup_ele()
    }

}


#[wasm_bindgen]
#[derive(Debug, Clone)]
pub struct WasmSegment {
    inner: Segment,
}

#[wasm_bindgen]
impl WasmSegment {

    #[wasm_bindgen(constructor)]
    pub fn new(passing_type: usize, length: f64, grade: f64, spl: f64, is_hc: bool, volume: f64, volume_op: f64, flow_rate: f64, flow_rate_o: f64, capacity: i32,
        ffs: f64, avg_speed: f64, vertical_class: i32, wasm_subsegments: Vec<WasmSubSegment>, phf: f64, phv: f64, pf: f64, fd: f64, fd_mid: f64, hor_class: i32) -> Self {

        let mut subsegments: Vec<SubSegment> = vec![];

        for (index, _) in wasm_subsegments.iter().enumerate() {

            let js_subsegment = wasm_subsegments[index].to_js_value();

            let subsegment: SubSegment = serde_wasm_bindgen::from_value(js_subsegment).unwrap();
            subsegments.push(subsegment);
        }

        WasmSegment {
            inner: Segment::new(
                passing_type,
                length,
                grade,
                spl,
                is_hc,
                volume,
                volume_op,
                flow_rate,
                flow_rate_o,
                capacity,
                ffs,
                avg_speed,
                vertical_class,
                subsegments,
                phf,
                phv,
                pf,
                fd,
                fd_mid,
                hor_class,
            ),
        }
    }


    pub fn subsegs_to_js_value(&self) -> JsValue {
        let js_array = js_sys::Array::new();

        let subsegments = self.inner.get_subsegments();

        for (_, subseg) in subsegments.iter().enumerate() {

            let obj = js_sys::Object::new();
            js_sys::Reflect::set(&obj, &JsValue::from_str("length"), &JsValue::from(subseg.get_length())).unwrap();
            js_sys::Reflect::set(&obj, &JsValue::from_str("avg_speed"), &JsValue::from(subseg.get_avg_speed())).unwrap();
            js_sys::Reflect::set(&obj, &JsValue::from_str("hor_class"), &JsValue::from(subseg.get_hor_class())).unwrap();
            js_sys::Reflect::set(&obj, &JsValue::from_str("design_rad"), &JsValue::from(subseg.get_design_rad())).unwrap();
            js_sys::Reflect::set(&obj, &JsValue::from_str("central_angle"), &JsValue::from(subseg.get_central_angle())).unwrap();
            js_sys::Reflect::set(&obj, &JsValue::from_str("sup_ele"), &JsValue::from(subseg.get_sup_ele())).unwrap();
            
            // Convert the JavaScript object to a JsValue
            js_array.push(&obj);
        }

        // for subseg in subsegments {
        //     let subseg_js_value = subseg[index].to_js_value();

        //     js_array.push(&subseg_js_value);
        // }

        JsValue::from(js_array)
    }


    pub fn to_js_value(&self) -> JsValue {
        let obj = js_sys::Object::new();
        js_sys::Reflect::set(&obj, &JsValue::from_str("passing_type"), &JsValue::from(self.get_passing_type())).unwrap();
        js_sys::Reflect::set(&obj, &JsValue::from_str("length"), &JsValue::from(self.get_length())).unwrap();
        js_sys::Reflect::set(&obj, &JsValue::from_str("grade"), &JsValue::from(self.get_grade())).unwrap();
        js_sys::Reflect::set(&obj, &JsValue::from_str("spl"), &JsValue::from(self.get_spl())).unwrap();
        js_sys::Reflect::set(&obj, &JsValue::from_str("is_hc"), &JsValue::from(self.get_is_hc())).unwrap();
        js_sys::Reflect::set(&obj, &JsValue::from_str("volume"), &JsValue::from(self.get_volume())).unwrap();
        js_sys::Reflect::set(&obj, &JsValue::from_str("volume_op"), &JsValue::from(self.get_volume_op())).unwrap();
        js_sys::Reflect::set(&obj, &JsValue::from_str("flow_rate"), &JsValue::from(self.get_flow_rate())).unwrap();
        js_sys::Reflect::set(&obj, &JsValue::from_str("flow_rate_o"), &JsValue::from(self.get_flow_rate_o())).unwrap();
        js_sys::Reflect::set(&obj, &JsValue::from_str("capacity"), &JsValue::from(self.get_capacity())).unwrap();
        js_sys::Reflect::set(&obj, &JsValue::from_str("ffs"), &JsValue::from(self.get_ffs())).unwrap();
        js_sys::Reflect::set(&obj, &JsValue::from_str("avg_speed"), &JsValue::from(self.get_avg_speed())).unwrap();
        js_sys::Reflect::set(&obj, &JsValue::from_str("vertical_class"), &JsValue::from(self.get_vertical_class())).unwrap();
        js_sys::Reflect::set(&obj, &JsValue::from_str("subsegments"), &self.get_subsegments()).unwrap();
        js_sys::Reflect::set(&obj, &JsValue::from_str("phf"), &JsValue::from(self.get_phf())).unwrap();
        js_sys::Reflect::set(&obj, &JsValue::from_str("phv"), &JsValue::from(self.get_phv())).unwrap();
        js_sys::Reflect::set(&obj, &JsValue::from_str("pf"), &JsValue::from(self.get_percent_followers())).unwrap();
        js_sys::Reflect::set(&obj, &JsValue::from_str("fd"), &JsValue::from(self.get_followers_density())).unwrap();
        js_sys::Reflect::set(&obj, &JsValue::from_str("fd_mid"), &JsValue::from(self.get_followers_density_mid())).unwrap();
        js_sys::Reflect::set(&obj, &JsValue::from_str("hor_class"), &JsValue::from(self.get_hor_class())).unwrap();

        JsValue::from(obj)
    }

    pub fn get_passing_type(&self) -> usize {
        self.inner.get_passing_type()
    }

    pub fn get_length(&self) -> f64 {
        self.inner.get_length()
    }

    pub fn get_grade(&self) -> f64 {
        self.inner.get_grade()
    }

    pub fn get_spl(&self) -> f64 {
        self.inner.get_spl()
    }

    pub fn get_is_hc(&self) -> bool {
        self.inner.get_is_hc()
    }

    pub fn get_volume(&self) -> f64 {
        self.inner.get_volume()
    }

    pub fn get_volume_op(&self) -> f64 {
        self.inner.get_volume_op()
    }

    pub fn get_flow_rate(&self) -> f64 {
        self.inner.get_flow_rate()
    }

    // // pub fn set_flow_rate(&mut self, flow_rate: f64) {
        
    // // }

    pub fn get_flow_rate_o(&self) -> f64 {
        self.inner.get_flow_rate_o()
    }

    // // pub fn set_flow_rate_o(&mut self, flow_rate_o: f64) {
        
    // // }

    pub fn get_capacity(&self) -> i32 {
        self.inner.get_capacity()
    }

    // // pub fn set_capacity(&mut self, capacity: i32) {
    // //     self.capacity = capacity
    // // }

    pub fn get_ffs(&self) -> f64 {
        self.inner.get_ffs()
    }

    // // pub fn set_ffs(&mut self, ffs: f64) {
    // //     self.ffs = ffs
    // // }

    pub fn get_avg_speed(&self) -> f64 {
        self.inner.get_avg_speed()
    }

    // // pub fn set_avg_speed(&mut self, avg_speed: f64) {
    // //     self.avg_speed = avg_speed
    // // }

    pub fn get_subsegments(&self) -> JsValue {
        self.subsegs_to_js_value()
    }

    pub fn get_vertical_class(&self) -> i32 {
        self.inner.get_vertical_class()
    }
    
    // // pub fn set_vertical_class(&mut self, vertical_class: i32) {
    // //     self.vertical_class = vertical_class
    // // }

    pub fn get_phf(&self) -> f64 {
        self.inner.get_phf()
    }

    pub fn get_phv(&self) -> f64 {
        self.inner.get_phv()
    }

    pub fn get_percent_followers(&self) -> f64 {
        self.inner.get_percent_followers()
    }

    // // pub fn set_percent_followers(&mut self, pf: f64) {
    // //    self.pf = pf
    // // }

    pub fn get_followers_density(&self) -> f64 {
        self.inner.get_followers_density()
    }

    // // pub fn set_followers_density(&mut self, fd: f64) {
    // //     self.fd = fd
    // // }

    pub fn get_followers_density_mid(&self) -> f64 {
        self.inner.get_followers_density_mid()
    }
    pub fn get_hor_class(&self) -> i32 {
        self.inner.get_hor_class()
    }

}


#[wasm_bindgen]
#[derive(Debug, Clone)]
pub struct WasmTwoLaneHighways{
    inner: TwoLaneHighways,
}

#[wasm_bindgen]
impl WasmTwoLaneHighways {

    #[wasm_bindgen(constructor)]
    pub fn new(wasm_segments: Vec<WasmSegment>, lane_width: f64, shoulder_width: f64, apd: f64, pmhvfl: f64, l_de: f64) -> Self {

        let mut segments: Vec<Segment> = vec![];

        for (index, _) in wasm_segments.iter().enumerate() {

            // let cloned_subsegments = wasm_subsegments.clone();

            let js_segment = wasm_segments[index].to_js_value();
            
            let segment: Segment = serde_wasm_bindgen::from_value(js_segment).unwrap();
            segments.push(segment);
        }

        WasmTwoLaneHighways {
            inner: TwoLaneHighways::new(
                segments, 
                lane_width, 
                shoulder_width, 
                apd, 
                pmhvfl, 
                l_de
            ),
        }
    }

    pub fn segs_to_js_value(&self) -> JsValue {
        let js_array = js_sys::Array::new();

        let segments = self.inner.get_segments();

        for (_, seg) in segments.iter().enumerate() {
            let sub_js_array = js_sys::Array::new();

            let obj = js_sys::Object::new();
            
            js_sys::Reflect::set(&obj, &JsValue::from_str("passing_type"), &JsValue::from(seg.get_passing_type())).unwrap();
            js_sys::Reflect::set(&obj, &JsValue::from_str("length"), &JsValue::from(seg.get_length())).unwrap();
            js_sys::Reflect::set(&obj, &JsValue::from_str("grade"), &JsValue::from(seg.get_grade())).unwrap();
            js_sys::Reflect::set(&obj, &JsValue::from_str("spl"), &JsValue::from(seg.get_spl())).unwrap();
            js_sys::Reflect::set(&obj, &JsValue::from_str("is_hc"), &JsValue::from(seg.get_is_hc())).unwrap();
            js_sys::Reflect::set(&obj, &JsValue::from_str("volume"), &JsValue::from(seg.get_volume())).unwrap();
            js_sys::Reflect::set(&obj, &JsValue::from_str("volume_op"), &JsValue::from(seg.get_volume_op())).unwrap();
            js_sys::Reflect::set(&obj, &JsValue::from_str("flow_rate"), &JsValue::from(seg.get_flow_rate())).unwrap();
            js_sys::Reflect::set(&obj, &JsValue::from_str("flow_rate_o"), &JsValue::from(seg.get_flow_rate_o())).unwrap();
            js_sys::Reflect::set(&obj, &JsValue::from_str("capacity"), &JsValue::from(seg.get_capacity())).unwrap();
            js_sys::Reflect::set(&obj, &JsValue::from_str("ffs"), &JsValue::from(seg.get_ffs())).unwrap();
            js_sys::Reflect::set(&obj, &JsValue::from_str("avg_speed"), &JsValue::from(seg.get_avg_speed())).unwrap();
            js_sys::Reflect::set(&obj, &JsValue::from_str("vertical_class"), &JsValue::from(seg.get_vertical_class())).unwrap();
            for (_, subseg) in seg.get_subsegments().iter().enumerate() {
                let sub_obj = js_sys::Object::new();
                js_sys::Reflect::set(&sub_obj, &JsValue::from_str("length"), &JsValue::from(subseg.get_length())).unwrap();
                js_sys::Reflect::set(&sub_obj, &JsValue::from_str("avg_speed"), &JsValue::from(subseg.get_avg_speed())).unwrap();
                js_sys::Reflect::set(&sub_obj, &JsValue::from_str("hor_class"), &JsValue::from(subseg.get_hor_class())).unwrap();
                js_sys::Reflect::set(&sub_obj, &JsValue::from_str("design_rad"), &JsValue::from(subseg.get_design_rad())).unwrap();
                js_sys::Reflect::set(&sub_obj, &JsValue::from_str("central_angle"), &JsValue::from(subseg.get_central_angle())).unwrap();
                js_sys::Reflect::set(&sub_obj, &JsValue::from_str("sup_ele"), &JsValue::from(subseg.get_sup_ele())).unwrap();
                sub_js_array.push(&sub_obj);
            }
            js_sys::Reflect::set(&obj, &JsValue::from_str("subsegments"), &JsValue::from(sub_js_array)).unwrap();
            js_sys::Reflect::set(&obj, &JsValue::from_str("phf"), &JsValue::from(seg.get_phf())).unwrap();
            js_sys::Reflect::set(&obj, &JsValue::from_str("phv"), &JsValue::from(seg.get_phv())).unwrap();
            js_sys::Reflect::set(&obj, &JsValue::from_str("pf"), &JsValue::from(seg.get_percent_followers())).unwrap();
            js_sys::Reflect::set(&obj, &JsValue::from_str("fd"), &JsValue::from(seg.get_followers_density())).unwrap();
            js_sys::Reflect::set(&obj, &JsValue::from_str("fd_mid"), &JsValue::from(seg.get_followers_density_mid())).unwrap();
            js_sys::Reflect::set(&obj, &JsValue::from_str("hor_class"), &JsValue::from(seg.get_hor_class())).unwrap();

            // Convert the JavaScript object to a JsValue
            js_array.push(&obj);
        }

        // for subseg in subsegments {
        //     let subseg_js_value = subseg[index].to_js_value();

        //     js_array.push(&subseg_js_value);
        // }

        JsValue::from(js_array)
    }

    pub fn get_segments(&self) -> JsValue {
        self.segs_to_js_value()
    }
    
    pub fn identify_vertical_class(&mut self, seg_num: usize) -> Vec<f64> {
        let mut _min = 0.0;
        let mut _max = 0.0;
        (_min, _max) = self.inner.identify_vertical_class(seg_num);
        vec![_min, _max]
    }

    pub fn determine_demand_flow(&mut self, seg_num: usize) -> Vec<f64> {
        let (demand_flow_i , demand_flow_o, capacity) = self.inner.determine_demand_flow(seg_num);

        vec![demand_flow_i, demand_flow_o, capacity as f64]
    }

    pub fn determine_vertical_alignment(&mut self, seg_num: usize) -> i32 {
        self.inner.determine_vertical_alignment(seg_num)
    }

    pub fn determine_free_flow_speed(&mut self, seg_num: usize) -> f64 {
        self.inner.determine_free_flow_speed(seg_num)
    }

    pub fn estimate_average_speed(&mut self, seg_num: usize) -> Vec<f64> {
        let (res_s, seg_hor_class) = self.inner.estimate_average_speed(seg_num);
        vec![res_s, seg_hor_class as f64]
    }

    pub fn estimate_percent_followers(&mut self, seg_num: usize) -> f64 {
        self.inner.estimate_percent_followers(seg_num)
    }

    pub fn estimate_average_speed_sf(&mut self, seg_num: usize, length: f64, vd: f64, phv: f64, rad: f64, sup_ele: f64) -> Vec<f64> {
        let (s, hor_class) = self.inner.estimate_average_speed_sf(seg_num, length, vd, phv, rad, sup_ele);
        vec![s, hor_class as f64]
    }

    pub fn estimate_percent_followers_sf(&self, seg_num: usize, vd: f64, phv: f64) -> f64 {
        self.inner.estimate_percent_followers_sf(seg_num, vd, phv)
    }

    pub fn determine_follower_density_pl(&mut self, seg_num: usize) -> Vec<f64> {
        let (fd, fd_mid) = self.inner.determine_follower_density_pl(seg_num);
        vec![fd, fd_mid]
    }

    pub fn determine_follower_density_pc_pz(&mut self, seg_num: usize) -> f64 {
        self.inner.determine_follower_density_pc_pz(seg_num)
    }

    pub fn determine_adjustment_to_follower_density(&mut self, seg_num: usize) -> f64 {
        self.inner.determine_adjustment_to_follower_density(seg_num)
    }

    pub fn determine_segment_los(&self, seg_num: usize, s_pl: f64, cap: i32) -> char {
        self.inner.determine_segment_los(seg_num, s_pl, cap)
    }

    pub fn determine_facility_los(&self, fd: f64, s_pl: f64) -> char {
        self.inner.determine_facility_los(fd, s_pl)
    }
}