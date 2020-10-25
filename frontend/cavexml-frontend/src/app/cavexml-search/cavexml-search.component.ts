import { Component, OnInit } from '@angular/core';
import data from '../../../data/data.json';


interface Cave {
        index: number
        country_name: string
        state_or_province: string
        phys_area_name: string
        principal_cave_name: string
        other_cave_name: string
        latitude: number
        longitude: number
        altitude: string
        length: string
        vertical_extent: string
        rock_type: string
        contents: string
        comments: string
        reference: string
        cave_use: string
        number_of_entrances: string
        branch_name: string
        cave_system: string
        ice_deposit_type: string
        cave_type: string
        altitude_max: number
        altitude_min: number
        vertical_extent_max: number
        vertical_extent_min: number
        length_max: number
        length_min: number
}

function getCaves(): Promise<Cave[]> {
  console.log("getting some caves")
  return fetch('http://localhost:5000/caves')
         // the JSON body is taken from the response
         .then(res => res.json())
         .then(res => {
                 // The response has an `any` type, so we need to cast
                 // it to the `User` type, and return it from the promise
                 console.log("got some caves", res)
                 // window.alert(
                 //   "tag: " + this.tag +
                 //   "\nlength: " + this.length +
                 //   "\nvertical_extent: " + this.vertical_extent +
                 //   "\naltitude: " + this.altitude +
                 //   "\nlength_gtlt: " + this.length_gtlt +
                 //   "\nvertical_extent_gtlt: " + this.vertical_extent_gtlt +
                 //   "\naltitude_gtlt: " + this.altitude_gtlt
                 // );
                 return res as Cave[]


         })
}

@Component({
  selector: 'app-cavexml-search',
  templateUrl: './cavexml-search.component.html',
  styleUrls: ['./cavexml-search.component.scss']
})
export class CavexmlSearchComponent implements OnInit {
  public tag;
  public length;
  public vertical_extent;
  public altitude;
  public length_gtlt;
  public vertical_extent_gtlt;
  public altitude_gtlt;

  // when Submit button is pressed
  onClickMe() {
    getCaves()
    // let caves: Cave[] = getCaves()
    // console.log("caves: ", caves)
    // // window.alert(
    //   "tag: " + this.tag +
    //   "\nlength: " + this.length +
    //   "\nvertical_extent: " + this.vertical_extent +
    //   "\naltitude: " + this.altitude +
    //   "\nlength_gtlt: " + this.length_gtlt +
    //   "\nvertical_extent_gtlt: " + this.vertical_extent_gtlt +
    //   "\naltitude_gtlt: " + this.altitude_gtlt
    // );

  }

  // when length value is entered
  OnInputLen(value) {
    this.length = value;
  }

  // when vertical_extent value is entered
  OnInputVE(value) {
    this.vertical_extent = value;
  }

  // when altitude value is entered
  OnInputAlt(value) {
    this.altitude = value;
  }

  // This is dummy data
  public dummyData = [
    {
      name: 'Test Cave 1',
      tags: 'Cave, SSSI',
      length: 112,
      vr: 22,
      altitude: 123
    },
    {
      name: 'Test Cave 2',
      tags: 'Cave, SSSI',
      length: 112,
      vr: 22,
      altitude: 123
    },
    {
      name: 'Test Cave 3',
      tags: 'Cave, SSSI',
      length: 112,
      vr: 22,
      altitude: 123
    },
  ];

  constructor() {
    this.dummyData = data
    // console.log('Reading local json files');
    // console.log(data);
  }

  ngOnInit() {
  }
  p: number = 1;

}
