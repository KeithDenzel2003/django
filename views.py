from django.shortcuts import render
from django.http import HttpResponse

def mission_view(request):
    mission = "This is about CCMS mission"
    mission = "Exploring Educational Innovation at Enverga University In the ever-evolving landscape of education, Enverga University remains dedicated to fostering excellence through cutting-edge instructional strategies and the integration of recent technologies. Throughout the academic year, the University has embraced innovative educational tools to enhance both synchronous learning sessions and asynchronous modules. Let's delve into the realm of educational technology that is shaping the academic experience at Enverga University. "
    mission = "Promoting IT Trends and Community Engagement As a key component of the University’s commitment to promoting awareness of the latest IT trends and extending community services, CCMS has launched MSEUF-ITCCE. This program aims to provide free specialized IT short courses to the vibrant community of Quezon, ensuring that knowledge and innovation reach every corner of our province. "
    return HttpResponse(mission)

def vision_view(request):
    vision = "This is about CCMS vision"
    vision = "Enverga University achieved Autonomous Status from the Commission on Higher Education, a distinction that speaks volumes about the institution's commitment to academic independence, innovative programs, and global competitiveness. The University is one of the first autonomous higher education institutions in the country that has maintained the recognition up to May 2023. "
    vision = "It is always the first approach of MSEUF to look for possibilities of organizing the participants-recipients into cohesive working groups or sectors. Each organized group or sector has its own specific needs or problems to be addressed, e.g. out-of-school youth, mothers’ club."
    return HttpResponse(vision)

def objectives_view(request):
    objectives = "This is about CCMS objectives"
    objectives = "Enverga University has taken a significant step towards ensuring and elevating the quality of its education in the recently concluded accreditation visit of the Philippine Association of Colleges and Universities Commission on Accreditation (PACUCOA) with six academic programs aiming for Level IV and two for Level III reaccreditation."
    objectives = "Reduce pilferage to 1% or less of the library collection every year for the next five years, Hold at least three (3) activities in the promotion of library services encouraging users and clients to go to the library every year for the next five years. "
    return HttpResponse(objectives)