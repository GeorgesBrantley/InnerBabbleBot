# -*- coding: utf-8 -*-
import groupMeFeatures
import groupMe
import operator

def sumOfLikesinGroup():
    # Has a corresponding view
    # gets values from Sessions
    comments = session.dictComments
    # sends values to bigger function in groupMeFeatures.py
    sumLikes = groupMeFeatures.getSumofLikes(comments)
    # shows output on view
    return dict(sum = sumLikes)

def groupMarkov():
    # Display Markov Chains for entire Group
    comments = session.dictComments # get comments
    results = groupMeFeatures.createMarkChain('all',10,comments)
    richResponse = []
    for x in results:
        richResponse.append('Group Markov Chain: ' + x)
    return dict(marks = results, rich = richResponse)


def likesRecievedPerUser():
    userDict = groupMeFeatures.getLikesPerUser(session.dictComments, session.translator)
    richResponse = 'Member Rankings by Total Likes Recieved:\n\n'
    for k,v in sorted(userDict.items(), key=lambda x: x[1], reverse=True):
        richResponse += k + ': ' + str(v) + ' Total Likes Recieved\n'
    return dict(m=userDict, rich = richResponse)

def numComments():
    coms = session.dictComments
    #id = inout
    #inputId = 19191585
    ans = groupMeFeatures.countCommentsPerUser(coms, session.translator)
    richResponse = 'Number Of Comments Per Member:\n'
    for k,v in sorted(ans.items(), key=lambda x: x[1], reverse=True):
        richResponse += k + ' has ' + str(v) + ' Comments!\n'

    return dict(ans=ans, gn = session.groupName, rich = richResponse)

def pastName():
    coms = session.dictComments
    oldNames,newNames = groupMeFeatures.getPastName(coms)
    richRes = "Past Names of Members\n\n"
    y = 0
    for x in oldNames:
        richRes += x + " --> " + newNames[y] + "\n"
        y += 1
    return dict(past = oldNames, future = newNames, rich = richRes)

def numKicked():
    coms = session.dictComments
    kickers,kicked = groupMeFeatures.getNumKicked(coms)
    richV = 'List of Victims (Number of Times They\'ve Been Kicked):\n\n'
    richK = 'List of Bullies (Number of Times They Removed Someone):\n\n'
    for k,v in sorted(kickers.items(), key=lambda x: x[1], reverse=True):
        richK += " " + k + ": " + str(v) + " People Kicked\n"
    for k,v in sorted(kicked.items(), key=lambda x: x[1], reverse=True):
        richV += " " + k + ": " + str(v) + " Times Kicked\n"
    return dict(kickers=kickers,kicked=kicked, richVictim=richV, richKicker = richK)

def mostGivingUsers():
    userDict = groupMeFeatures.mostGivingUsers(session.dictComments, session.translator)
    richResponse = 'Member Rankings by Total Likes Given:\n\n'
    for k,v in sorted(userDict.items(), key=lambda x: x[1], reverse=True):
        richResponse += k + ': ' + str(v) + ' Total Likes Given\n'
    return dict(m=userDict, rich = richResponse)

def likesPerComment():
    ratio = groupMeFeatures.getLikesPerComment(session.dictComments,session.translator)
    richResponse = 'Member Rankings by Average Likes Per Comment:\n\n'
    for k,v in sorted(ratio.items(), key=lambda x: x[1], reverse=True):
        richResponse += k + ': ' + str(v) + ' Likes/Comment\n'
    return dict(m=ratio, rich = richResponse)

def specificLikes():
    # a user's secret crush
    userDict = groupMeFeatures.specificLikesGiven(session.dictComments, session.translator)
    richResponse = 'Secret Crushes (Who Users Like The Most):\n\n'
    for k,v in userDict.iteritems():
        richResponse += '\n' + k + "'s Secret Crushes:\n"
        limit = 0
        for kk,vv in  sorted(v[0].items(), key=lambda x: x[1], reverse=True):
            limit += 1
            if limit > 3:
                break
            richResponse += kk + ': ' + str(vv) + ' Comments Liked\n'
    return dict(m=userDict, rich = richResponse)


def specificLikesRec():
    userDict = groupMeFeatures.specificLikesRec(session.dictComments, session.translator)
    richResponse = 'Secret Crushes (Who Likes Certain Member The Most):\n\n'
    for k,v in userDict.iteritems():
        richResponse += '\n' + k + "'s Secret Admirers:\n"
        limit = 0
        for kk,vv in  sorted(v[0].items(), key=lambda x: x[1], reverse=True):
            limit += 1
            if limit > 3:
                break
            richResponse +=  kk + ': ' + str(vv) + ' Comments Liked\n'
    return dict(m=userDict, rich = richResponse)

def groupMedals():
    numUsers = len(groupMe.getListOfUsers(session.myAuth,session.myGroupID))
    userDict,medalRange = groupMeFeatures.getMedalCount("", session.dictComments, session.translator,numUsers)
    # Create Responses
    richPlatResponse = 'Platinum Medals (100% Likes):\n'
    richGoldResponse = 'Gold Medals (75% Likes):\n'
    richSilvResponse = 'Silver Medals (50% Likes):\n'
    richBronResponse = 'Bronze Medals (25% Likes):\n'
    
    medals = ['Platinum','Gold','Silver','Bronze']
    richResponses = [richPlatResponse,richGoldResponse,richSilvResponse,richBronResponse]
    right = 0
    for mm in medals:
        for k,vv in sorted(userDict.items(), key=lambda x: x[1][mm], reverse=True):
            if vv[mm] != 0:
                richResponses[right] += k + ' Has Earned ' + str(vv[mm]) + ' ' + mm
                if vv[mm] > 1:
                    richResponses[right] += ' Medals!\n'
                else:
                    richResponses[right] += 'Medal!\n'
        right += 1
    
    colors = ['#e5e4e2','#DAA520','#C0C0C0','#cd7f32']
    return dict(r=medalRange,m=userDict,medals=medals, gn = session.groupName, riches = richResponses, colors=colors)
