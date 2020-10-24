import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CavexmlSearchComponent } from './cavexml-search.component';

describe('CavexmlSearchComponent', () => {
  let component: CavexmlSearchComponent;
  let fixture: ComponentFixture<CavexmlSearchComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CavexmlSearchComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CavexmlSearchComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
