from abc import ABC, abstractmethod
import numpy as np
from anahiepro.pairwise import PairwiseComparisonMatrix

# TODO: change the shape of 

class Node(ABC):
    def __init__(self, name, parents=None, children=None, id=0, pcm=None):
        """
        Initialize a Node object.
        
        Parameters
        ----------
        name : str
            Name of the node.
        parents : list, optional
            List of parent nodes (default is None).
        children : list, optional
            List of child nodes (default is None).
        id : int, optional
            Unique identifier for the node (default is 0).
        """
        self._id = id
        self._name = name
        self._parents = []
        self._children = []
        self.pcm = None
        
        if children:
            for child in children:
                self.add_child(child)

        if parents:
            for parent in parents:
                self._parents.append(parent)
        
        self._set_pcm(pcm)

    
    def __copy__(self):
        instance = type(self)(self._name)
        instance.pcm = self.pcm
        return instance


    def get_name(self):
        """
        Get the name of the node.
        
        Returns
        -------
        str
            Name of the node.
        """
        return self._name
    

    def get_parents(self):
        """
        Get the list of parent nodes.
        
        Returns
        -------
        list
            List of parent nodes.
        """
        return self._parents
    

    def get_children(self):
        """
        Get the list of child nodes.
        
        Returns
        -------
        list
            List of child nodes.
        """
        return self._children
    

    @abstractmethod
    def get_key(self):
        pass


    @abstractmethod
    def add_child(self, child):
        """
        Add a child node. This method should be implemented by subclasses.
        
        Parameters
        ----------
        child : Node
            Child node to be added.
        """
        pass
    

    def _add_parent(self, parent):
        """
        Add a parent node if it can be added.
        
        Parameters
        ----------
        parent : Node
            Parent node to be added.
        """
        if self._can_add(parent):
            self._parents.append(parent)
    

    def _check_append_condision(self, item):
        """
        Check if the item can be appended as a child.
        
        Parameters
        ----------
        item : Node
            Item to be checked.
        
        Raises
        ------
        TypeError
            If item cannot be added as a child.
        """
        if not self._can_add(item):
            raise TypeError("The child must be a 'Node' instance.")
        
        if self._is_Problem(item):
            raise TypeError("The child cannot be 'Problem' object instance.")
    

    def _can_add(self, item):
        """
        Check if the item can be added as a node.
        
        Parameters
        ----------
        item : object
            Item to be checked.
        
        Returns
        -------
        bool
            True if item can be added, False otherwise.
        """
        return isinstance(item, Node)
    

    def _is_Problem(self, item):
        """
        Check if the item is an instance of Problem.
        
        Parameters
        ----------
        item : object
            Item to be checked.
        
        Returns
        -------
        bool
            True if item is an instance of Problem, False otherwise.
        """
        return isinstance(item, Problem)
    

    def show(self):
        """
        Show the node and its children in a hierarchical structure.
        
        Parameters
        ----------
        depth : int, optional
            Depth level for display (default is 0).
        
        Returns
        -------
        str
            Hierarchical representation of the node.
        """
        return self._show(0) 
    

    def _show(self, depth):
        graph = '+' + ('--' * depth) + self.__str__()
        for child in self._children:
            graph += child._show(depth + 1)
        return graph
    

    def compare(self, key: tuple):
        """
        Compare the node with a given key.
        
        Parameters
        ----------
        key : tuple
            Tuple containing name and id to compare.
        
        Returns
        -------
        bool
            True if name and id match the key, False otherwise.
        """
        if len(key) != 2:
            return False
        
        return self._name == key[0] and self._id == key[1]
    

    def create_pcm(self):
        """
        Create a Pairwise Comparison Matrix (PCM) for the node.
        """
        if self.pcm and len(self.pcm.matrix) == len(self._children):
            return
        
        self.pcm = PairwiseComparisonMatrix(len(self._children))
    

    def set_matrix(self, matrix):
        """
        Set the matrix for the PCM.
        
        Parameters
        ----------
        matrix : np.ndarray
            Matrix to be set.
        """
        if not self.pcm:
            self.create_pcm()
        
        if np.array(matrix).shape != (self.pcm.size, self.pcm.size):
            raise ValueError("The shape of matrix do not match.")

        self.pcm.set_matrix(matrix)
    
    def _set_pcm(self, pcm):
        if not pcm:
            return
        
        if isinstance(pcm, PairwiseComparisonMatrix):
            self.pcm = PairwiseComparisonMatrix(size=len(pcm.matrix), matrix=pcm.matrix)
        else:
            self.pcm = PairwiseComparisonMatrix(size=len(pcm), matrix=pcm)
        
        
    def set_comparison(self, i, j, value):
        """
        Set a comparison value in the PCM.
        
        Parameters
        ----------
        i : int
            Index of the first element.
        j : int
            Index of the second element.
        value : float
            Comparison value.
        """
        if self.pcm:
            self.pcm.set_comparison(i, j, value)
    

    def get_priority_vector(self):
        """
        Get the priority vector from the PCM.
        
        Returns
        -------
        np.ndarray
            Priority vector if PCM exists, None otherwise.
        """
        if self.pcm:
            return self.pcm.calculate_priority_vector()
    

    def get_consistency_ratio(self):
        """
        Get the consistency ratio from the PCM.
        
        Returns
        -------
        float
            Consistency ratio if PCM exists, None otherwise.
        """
        if self.pcm:
            return self.pcm.calculate_consistency_ratio()
    

    def get_pcm(self):
        """
        Get the matrix from the PCM.
        
        Returns
        -------
        np.ndarray
            Matrix if PCM exists, None otherwise.
        """
        if not self.pcm:
            self.create_pcm()

        return self.pcm.matrix

    
    
    def __str__(self) -> str:
        return self._name + '\n'
    

    def __eq__(self, value) -> bool:
        return self._name == value._name and self._id == value._id
    

    def __hash__(self) -> int:
        return hash(self._name) + hash(self._id)
    
    
    def __repr__(self):
        return self._name


class Problem(Node):
    _problem_id = 0
    
    def __init__(self, name=None, children=None, pcm=None):
        """
        Initialize a Problem node.
        
        Parameters
        ----------
        name : str
            Name of the problem.
        children : list, optional
            List of child nodes (default is None).
        """
        if name is None:
            name = "Problem" + str(Problem._problem_id)

        super().__init__(name, None, children, id=Problem._problem_id, pcm=pcm)
        Problem._problem_id += 1
    

    def add_child(self, child):
        """
        Add a child node to the problem.
        
        Parameters
        ----------
        child : Node
            Child node to be added.
        """
        self._check_append_condision(child)
        self._children.append(child)
        child._add_parent(self)


    def get_key(self):
        return (self.get_name(), self._id)


class Criteria(Node):
    _criteria_id = 0
    
    def __init__(self, name=None, children=None, pcm=None):
        """
        Initialize a Criteria node.
        
        Parameters
        ----------
        name : str
            Name of the criteria.
        parents : list, optional
            List of parent nodes (default is None).
        children : list, optional
            List of child nodes (default is None).
        """
        if name is None:
            name = "Criteria" + str(Criteria._criteria_id)

        super().__init__(name, None, children, id=Criteria._criteria_id, pcm=pcm)
        Criteria._criteria_id += 1
    

    def add_child(self, child):
        """
        Add a child node to the criteria.
        
        Parameters
        ----------
        child : Node
            Child node to be added.
        """
        self._check_append_condision(child)
        self._children.append(child)
        child._add_parent(self)


    def get_key(self):
        return (self.get_name(), self._id)


class DummyCriteria(Criteria):
    _dummy_criteria_id  = 0
    def __init__(self):
        super().__init__("DummyCriteria" + str(DummyCriteria._dummy_criteria_id))
        Criteria._criteria_id -= 1


class Alternative(Node):
    _alternative_id = 0
    
    def __init__(self, name=None):
        """
        Initialize an Alternative node.
        
        Parameters
        ----------
        name : str
            Name of the alternative.
        """
        if name is None:
            name = "Alternative" + str(Alternative._alternative_id)

        super().__init__(name, id=Alternative._alternative_id)
        Alternative._alternative_id += 1
        del self.pcm
    

    def add_child(self, child):
        """
        Prevent adding a child node to the alternative.
        
        Parameters
        ----------
        child : Node
            Child node to be added.
        
        Raises
        ------
        NotImplementedError
            Always raised as Alternatives cannot have children.
        """
        raise NotImplementedError("The 'class Alternative(Node)' cannot have a child.")
    

    def create_pcm(self):
        """
        Prevent creating a PCM for the alternative.
        
        Raises
        ------
        NotImplementedError
            Always raised as Alternatives cannot have a PCM.
        """
        pass
    

    def set_matrix(self, matrix):
        """
        Prevent setting a matrix for the alternative.
        
        Parameters
        ----------
        matrix : np.ndarray
            Matrix to be set.
        
        Raises
        ------
        NotImplementedError
            Always raised as Alternatives cannot have a PCM.
        """
        raise NotImplementedError("The 'class Alternative(Node)' cannot have a 'PairwiseComparisonMatrix' instance.")
    

    def set_comparison(self, i, j, value):
        raise NotImplementedError("The 'class Alternative(Node)' cannot have a 'PairwiseComparisonMatrix' instance.")


    def get_key(self):
        return (self.get_name(), self._id)
