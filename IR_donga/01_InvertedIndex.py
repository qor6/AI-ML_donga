def Intersect_two_post_list(p1, p2):
  answer = []
  i, j = 0, 0
  while i != len(p1) and j != len(p2):
    if p1[i] == p2[j]:
      answer.append(p1[i])
      i += 1
      j += 1
    elif p1[i] < p2[j]:
      i += 1
    else:
      j += 1
  return answer


def intersect_optimized_for_query(tokens):
  # tokens sort
  def sort_by(tokens):
    result = dict(
        sorted(tokens.items(), key=lambda item: len(item[1]), reverse=False))
    return result

  terms = sort_by(tokens)
  # first post list
  result = terms[list(terms.keys())[0]]
  # first post list of terms
  del terms[list(terms.keys())[0]]
  while len(terms) != 0 and len(result) != 0:
    result = Intersect_two_post_list(result, terms[list(terms.keys())[0]])
    # first post list of terms
    del terms[list(terms.keys())[0]]
  return result


coffee = [5, 11, 20, 25, 30, 40, 52, 58]
colombia = [4, 20, 30, 37, 40]
tokens = {'coffee': coffee, 'colombia': colombia}
answer = Intersect_two_post_list(tokens['coffee'], tokens['colombia'])
print(answer)

Brutus = [1, 2, 4, 11, 31, 45, 173, 174]
Caesar = [4, 20, 30, 37, 40]
