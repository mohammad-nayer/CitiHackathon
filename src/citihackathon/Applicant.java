/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package citihackathon;

/**
 *
 * @author qhzrv
 */
public class Applicant 
{
    private String _appName;
    private String _appUniversity;
    private String _appDegree;
    private int _appAcademic;
    private int _appTechnicalExpertise;
    private int _appCommunicationSkills;
    private int _appLeadershipSkills;
    private int _appPlanning;
    
    
    public Applicant(String name, String uni, String degree, int academic, int techExpertise, int commSkills, int leaderSkills, int planning)
    {
        _appName = name;
        _appUniversity = uni;
        _appDegree = degree;
        _appAcademic = academic;
        _appTechnicalExpertise = techExpertise;
        _appCommunicationSkills = commSkills;
        _appLeadershipSkills = leaderSkills;
        _appPlanning = planning;
    }
    
    public String getName()
    {
        return _appName;
    }
    
    public String getUniversityName()
    {
        return _appUniversity;
    }
    
    public String getAppDegree()
    {
        return _appDegree;
    }
    
    public int getTechExpScore()
    {
        return _appTechnicalExpertise;
    }
    
    public int getCommunicationScore()
    {
        return _appCommunicationSkills;
    }
    
    public int getLeadershipScore()
    {
        return _appLeadershipSkills;
    }
    
    public int getPlanningScore()
    {
        return _appPlanning;
    }
}
    

