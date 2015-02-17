/**
 * \file MuShowerRecoStudy.h
 *
 * \ingroup scratch_ana
 * 
 * \brief Class def header for a class MuShowerRecoStudy
 *
 * @author davidkaleko
 */

/** \addtogroup scratch_ana

    @{*/

#ifndef LARLITE_MUSHOWERRECOSTUDY_H
#define LARLITE_MUSHOWERRECOSTUDY_H

#include "Analysis/ana_base.h"
#include "TH1.h"

namespace larlite {
  /**
     \class MuShowerRecoStudy
     User custom analysis class made by davidkaleko
   */
  class MuShowerRecoStudy : public ana_base{
  
  public:

    /// Default constructor
    MuShowerRecoStudy(){ 
      _name="MuShowerRecoStudy"; 
      _reco_minus_true_showers = 0;
      _nrecoshowers_whenNoMCShowers = 0;
      _fout=0;
    };

    /// Default destructor
    virtual ~MuShowerRecoStudy(){};

    /** IMPLEMENT in MuShowerRecoStudy.cc!
        Initialization method to be called before the analysis event loop.
    */ 
    virtual bool initialize();

    /** IMPLEMENT in MuShowerRecoStudy.cc! 
        Analyze a data event-by-event  
    */
    virtual bool analyze(storage_manager* storage);

    /** IMPLEMENT in MuShowerRecoStudy.cc! 
        Finalize method to be called after all events processed.
    */
    virtual bool finalize();

    protected:

    TH1F* _reco_minus_true_showers;
    TH1F* _nrecoshowers_whenNoMCShowers;
  };
}
#endif

//**************************************************************************
// 
// For Analysis framework documentation, read Manual.pdf here:
//
// http://microboone-docdb.fnal.gov:8080/cgi-bin/ShowDocument?docid=3183
//
//**************************************************************************

/** @} */ // end of doxygen group 
