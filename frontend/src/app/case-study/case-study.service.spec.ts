import { TestBed, inject } from '@angular/core/testing';

import { CaseStudyService } from './case-study.service';

describe('CaseStudyService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [CaseStudyService]
    });
  });

  it('should be created', inject([CaseStudyService], (service: CaseStudyService) => {
    expect(service).toBeTruthy();
  }));
});
