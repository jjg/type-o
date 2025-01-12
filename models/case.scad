/*
    Type-O writing device
*/

module keyboard(){
    rotate([180,0,0]){
        // keyboard mounting plate
        import("reference/planckplate_v2_tab_fix.stl");
    }
}

// lcd display
module 40x4_LCD(){
    // overall PCB
    color("green")
    cube([190,54,1.6]);
    
    // TODO: mounting holes (183x47)
    
    // bezel
    color("blue")
    translate([(190/2)-(166/2),(54/2)-(43.1/2),1]){
        cube([166.0,43.1,9]);
    }
    
    // viewing area
    color("white")
    translate([(190/2)-(147/2),(54/2)-(29.5/2),2]){
        cube([147,29.5,9]);
    }
    
    // TOOD: active area (140.45x23.16)
    
    // TODO: solder pads/pins
}

// TODO: lipo cell
// TODO: boost converter
// TODO: mode switch
// TODO: reset button

// case top
module case_top(){
    difference(){
        color("red")
        cube([250,165,10]);
        
        // hollow-out
        translate([(250/2)-(230/2)-5,(170/2)-(150/2)-5,-1]){
            cube([240,155,6]);
        }
        
        // lcd hole
        translate([(250/2)-(166/2)-1,105,0]){
            cube([168.0,44,12]);
        }
        
        // keyboad hole
        translate([(250/2)-(233/2)-1,8,-1]){
            cube([235,84,12]);
        }
        
        // USB-C hole
        translate([225,158,-1]){
            cube([15,15,8]);
        }
    }
    
    // TODO: keyboard retainer
    // TODO: LCD mounting posts
    // TODO: Feather mounting posts
}
// case bottom
module case_bottom(){
    difference(){
        color("red")
        //cube([250,165,10]);
        cube([250,165,30]);
        
        // electronics opening
        //translate([(250/2)-(230/2)-5,85,5]){
        translate([(250/2)-(230/2)-5,95,5]){
            //cube([240,75,6]);
            cube([240,65,30]);
        }
        
        // keyboard opening
        //translate([(250/2)-(235/2),8,8]){
        translate([(250/2)-(235/2),8,20]){
            //#cube([235,84,12]);
            cube([235,84,30]);
        }
        // cut-out under keyboard
        //translate([(250/2)-(227/2),12,5]){
        translate([(250/2)-(227/2),12,5]){
            //#cube([227,84,12]);
            cube([227,80,30]);
        }
        
        // keyboard wiring opening
        translate([(250/2)-(200/2),90,5]){
            cube([200,10,30]);
        }
        
        // TODO: reset hole
    }
        
}

// Assemble!
translate([-1,0,0]){
    //keyboard();
}

translate([-190/2,50,1]){
    //40x4_LCD();
}

translate([-250/2,-50,30]){
    //case_top();
}

translate([119,110,3]){
    rotate([0,180,90]){
        //import("reference/4884 Feather RP2040.stl");
    }
}

translate([-250/2,-50,-30]){
    case_bottom();
}
